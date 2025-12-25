import base64
import gzip
import hashlib
import json
import logging
import re
import subprocess
import zlib
from collections import deque
from collections.abc import Generator
from collections.abc import Iterable
from collections.abc import Iterator
from datetime import datetime
from itertools import islice
from pathlib import Path
from shutil import COPY_BUFSIZE
from typing import Any

import datamodel_code_generator
import frozendict
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import CBC
from cryptography.hazmat.primitives.padding import PKCS7
from datamodel_code_generator import DataModelType
from datamodel_code_generator import PythonVersion
from datamodel_code_generator.parser.jsonschema import JsonSchemaParser
from genson import SchemaBuilder
from genson import TypedSchemaStrategy
from mitmproxy.http import HTTPFlow
from mitmproxy.http import Message
from mitmproxy.http import Request

from . import config

logger = logging.getLogger(__name__)

etag_pattern = re.compile(r"^\"(?P<md5>[a-f\d]{32}):(?P<mtime>\d+(?:\.\d+)?)\"$")


def is_empty(iterable: Iterator) -> bool:
    try:
        next(iterable)
    except StopIteration:
        return True
    else:
        return False


def consume(iterable: Iterable, n: int | None = None) -> None:
    if n is None:
        deque(iterable, maxlen=0)
    else:
        next(islice(iterable, n, n), None)


def rmtree_empty(path: Path) -> None:
    for child in path.iterdir():
        if child.is_dir():
            rmtree_empty(child)
    if is_empty(path.iterdir()):
        path.rmdir()


def get_md5(path: Path) -> str:
    logger.debug("[MD5] %s", path)
    md5 = hashlib.md5(usedforsecurity=False)
    with path.open("rb") as file:
        while chunk := file.read(COPY_BUFSIZE):
            md5.update(chunk)
    return md5.hexdigest()


def check_md5(path: Path, expected_md5: str) -> bool:
    hash_path = (config.DATA_DIR / "hash" / path.relative_to(config.DATA_DIR)).with_suffix(".md5")

    if not hash_path.is_file():
        md5 = get_md5(path)
        hash_path.parent.mkdir(parents=True, exist_ok=True)
        hash_path.write_text(md5)
        return md5 == expected_md5

    if expected_md5 != hash_path.read_text():
        logger.warning("[MD5] %s", path)
        hash_path.unlink()
        return False

    return True


def decrypt_data(algorithm: AES, data: bytes, initialization_vector: bytes) -> bytes:
    decryptor = Cipher(algorithm, CBC(initialization_vector)).decryptor()
    unpadder = PKCS7(AES.block_size).unpadder()
    decrypted_data = decryptor.update(data) + decryptor.finalize()
    return unpadder.update(decrypted_data) + unpadder.finalize()


def is_valid_message(request: Request, message: Message) -> bool:
    return bool(
        request.pretty_host in {"api.doaxvv.com", "api.doax-venusvacation.jp"}
        and "X-DOAXVV-Encrypted" in message.headers
        and message.content
    )


def iter_messages(flow: HTTPFlow) -> Generator[Message]:
    for message in (flow.request, flow.response):
        if is_valid_message(flow.request, message):
            yield message


def decrypt_message(key: str, message: Message) -> bytes:
    decrypted_data = decrypt_data(
        AES(base64.b64decode(key)), message.content, base64.b64decode(message.headers["X-DOAXVV-Encrypted"])
    )
    return zlib.decompress(decrypted_data)


def decrypt_file(key: str, path: Path) -> bytes:
    decrypted_data = decrypt_data(AES(key.encode()), path.read_bytes(), bytes.fromhex(path.name))
    return gzip.decompress(decrypted_data)


class AbstractDateTime(TypedSchemaStrategy):
    FORMAT_STRING: str
    FORMAT_NAME: str

    JS_TYPE = "string"
    PYTHON_TYPE = (str,)

    @classmethod
    def match_schema(cls, schema: dict) -> bool:
        return super().match_schema(schema) and schema.get("format") == cls.FORMAT_NAME

    @classmethod
    def match_object(cls, obj: Any) -> bool:  # noqa: ANN401
        match = super().match_object(obj)
        if match:
            try:
                datetime.strptime(obj, cls.FORMAT_STRING)  # noqa: DTZ007
            except ValueError:
                match = False
        return match

    def to_schema(self) -> dict:
        schema = super().to_schema()
        schema["format"] = self.FORMAT_NAME
        return schema


class CustomDateTime(AbstractDateTime):
    FORMAT_STRING = "%Y-%m-%d %H:%M:%S"
    FORMAT_NAME = "date-time"


class CustomDate(AbstractDateTime):
    FORMAT_STRING = "%Y-%m-%d"
    FORMAT_NAME = "date"


class CustomTime(AbstractDateTime):
    FORMAT_STRING = "%H:%M:%S"
    FORMAT_NAME = "time"


class CustomSchemaBuilder(SchemaBuilder):
    EXTRA_STRATEGIES = CustomDateTime, CustomDate, CustomTime


def json_to_schema(dir: Path, json_dir: Path, schema_dir: Path) -> None:
    logger.info("[PATH] %s", dir)

    data_hashes = set()
    json_datas = []
    schema_builder = CustomSchemaBuilder()
    for json_path in dir.rglob("*.json"):
        logger.debug("[JSON] %s", json_path)

        with json_path.open("rb") as file:
            json_data = json.load(file)
        data_hash = frozendict.deepfreeze(json_data, {list: frozenset})
        if data_hash not in data_hashes:
            data_hashes.add(data_hash)
            json_datas.append(json_data)
            schema_builder.add_object(json_data)

    relative_path = dir.relative_to(json_dir)

    schema = schema_builder.to_schema()
    schema["title"] = "_".join(relative_path.parts[1:])
    schema["examples"] = json_datas

    schema_path = schema_dir / relative_path.with_suffix(".schema.json")
    logger.warning("[SCHEMA] %s", schema_path)

    schema_path.parent.mkdir(parents=True, exist_ok=True)
    with schema_path.open("w") as file:
        json.dump(schema, file, separators=(",", ":"))


def custom_class_name_generator(title: str) -> str:
    return f"{title.removesuffix('_list')}_model"


def schema_to_model(path: Path, schema_dir: Path, model_dir: Path) -> None:
    logger.info("[SCHEMA] %s", path)

    schema_data = path.read_text()
    data_model_types = datamodel_code_generator.model.get_data_model_types(
        DataModelType.PydanticBaseModel, PythonVersion.PY_313
    )
    parser = JsonSchemaParser(
        schema_data,
        data_model_type=data_model_types.data_model,
        data_model_root_type=data_model_types.root_model,
        data_model_field_type=data_model_types.field_model,
        data_type_manager_type=data_model_types.data_type_manager,
        dump_resolve_reference_action=data_model_types.dump_resolve_reference_action,
        base_class="naagin.bases.ModelBase",
        field_constraints=True,
        use_standard_collections=True,
        disable_appending_item_suffix=True,
        custom_class_name_generator=custom_class_name_generator,
        use_title_as_name=True,
        use_union_operator=True,
        formatters=[],
    )
    parsed_data = parser.parse()
    parsed_lines = parsed_data.split("\n")

    if config.EXAMPLES:
        future_import = "from pydantic import ConfigDict"
        json_data = json.loads(schema_data)
        examples = json_data["examples"]
        json_schema_extra = {"examples": examples}
        parsed_lines.append(f"    model_config = ConfigDict(json_schema_extra={json_schema_extra})")
        parsed_lines.append("")
    else:
        future_import = ""
    parsed_lines[0] = future_import
    model_data = "\n".join(parsed_lines)

    relative_path = path.relative_to(schema_dir).with_suffix("")
    model_path = model_dir / relative_path.with_suffix(".py")
    logger.warning("[MODEL] %s", model_path)

    model_path.parent.mkdir(parents=True, exist_ok=True)
    model_path.write_text(model_data, "utf-8")


def model_formatter(model_dir: Path) -> None:
    subprocess.run(("ruff", "format", model_dir), check=True)  # noqa: S603
