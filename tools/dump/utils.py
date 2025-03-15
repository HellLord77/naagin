import base64
import gzip
import json
import logging
import subprocess
import zlib
from collections import deque
from datetime import datetime
from itertools import islice
from pathlib import Path
from typing import Generator
from typing import Iterable

import datamodel_code_generator
import frozendict
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import CBC
from cryptography.hazmat.primitives.padding import PKCS7
from datamodel_code_generator import DataModelType
from datamodel_code_generator import PythonVersion
from datamodel_code_generator.model.pydantic import BaseModel
from datamodel_code_generator.parser.jsonschema import JsonSchemaParser
from genson import SchemaBuilder
from genson import TypedSchemaStrategy
from mitmproxy.http import HTTPFlow
from mitmproxy.http import Message
from mitmproxy.http import Request

import config


def consume(iterable: Iterable, n: int | None = None):
    if n is None:
        deque(iterable, maxlen=0)
    else:
        next(islice(iterable, n, n), None)


def decrypt_data(algorithm: AES, data: bytes, initialization_vector: bytes) -> bytes:
    decryptor = Cipher(algorithm, CBC(initialization_vector)).decryptor()
    unpadder = PKCS7(AES.block_size).unpadder()
    decrypted_data = decryptor.update(data) + decryptor.finalize()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()
    return unpadded_data


def is_valid_message(request: Request, message: Message) -> bool:
    return bool(
        request.pretty_host == "api.doaxvv.com"
        and "X-DOAXVV-Encrypted" in message.headers
        and message.content
    )


def iter_messages(flow: HTTPFlow) -> Generator[Message]:
    for message in (flow.request, flow.response):
        if is_valid_message(flow.request, message):
            yield message


def decrypt_message(key: str, message: Message) -> bytes:
    decrypted_data = decrypt_data(
        AES(base64.b64decode(key)),
        message.content,
        base64.b64decode(message.headers["X-DOAXVV-Encrypted"]),
    )
    uncompressed_data = zlib.decompress(decrypted_data)
    return uncompressed_data


def decrypt_file(key: str, path: Path) -> bytes:
    decrypted_data = decrypt_data(
        AES(key.encode()),
        path.read_bytes(),
        bytes.fromhex(path.name),
    )
    uncompressed_data = gzip.decompress(decrypted_data)
    return uncompressed_data


class AbstractDateTime(TypedSchemaStrategy):
    FORMAT_STRING: str
    FORMAT_NAME: str

    JS_TYPE = "string"
    PYTHON_TYPE = (str,)

    @classmethod
    def match_schema(cls, schema: dict) -> bool:
        return super().match_schema(schema) and schema.get("format") == cls.FORMAT_NAME

    @classmethod
    def match_object(cls, obj) -> bool:
        match = super().match_object(obj)
        if match:
            try:
                datetime.strptime(obj, cls.FORMAT_STRING)
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


def json_to_schema(dir: Path, json_dir: Path, schema_dir: Path):
    logging.info(f"[PATH] {dir}")

    data_hashes = set()
    json_datas = []
    schema_builder = CustomSchemaBuilder()
    for json_path in dir.rglob("*.json"):
        json_path: Path
        logging.debug(f"[JSON] {json_path}")

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
    logging.warning(f"[SCHEMA] {schema_path}")

    schema_path.parent.mkdir(parents=True, exist_ok=True)
    with schema_path.open("w") as file:
        json.dump(schema, file, separators=(",", ":"))


def custom_class_name_generator(title: str):
    return f"{title.removesuffix("_list")}_model"


def schema_to_model(path: Path, schema_dir: Path, model_dir: Path):
    logging.info(f"[SCHEMA] {path}")

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
        parsed_lines.append(
            f"    model_config = ConfigDict(json_schema_extra={json_schema_extra})"
        )
        parsed_lines.append("")
    else:
        future_import = ""
    parsed_lines[0] = future_import
    model_data = "\n".join(parsed_lines)

    relative_path = path.relative_to(schema_dir).with_suffix("")
    model_path = model_dir / relative_path.with_suffix(".py")
    logging.warning(f"[MODEL] {model_path}")

    model_path.parent.mkdir(parents=True, exist_ok=True)
    model_path.write_text(model_data, "utf-8")


def model_formatter(model_dir: Path):
    subprocess.run(("ruff", "format", model_dir), check=True)
