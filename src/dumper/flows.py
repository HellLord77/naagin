import base64
import functools
import glob
import hashlib
import logging
import shutil
import zlib
from pathlib import Path
from string import Formatter
from typing import Iterable

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from mitmproxy.http import HTTPFlow
from mitmproxy.http import Message
from mitmproxy.http import Request
from mitmproxy.io import FlowReader

import config
import utils

VARIABLE_PATHS = (
    "v1/dishevelment/{owner_id}/{item_mid}",
    "v1/friendship/{friend_id}",
    "v1/girl/{girl_mid}",
    "v1/item/consume/use/{item_mid}",
    "v1/item/equipment/type/{type}",
    "v1/max_combine/{owner_id}/{item_mid}",
    "v1/onsen/{onsen_mid}/entry/slot",
    "v1/onsen/{onsen_mid}/item/use/{item_mid}",
    "v1/onsen/{onsen_mid}/reward",
    "v1/onsen/{onsen_mid}/update/quality",
    "v1/owner/detail/{owner_id}",
    "v1/owner/episode/{episode_mid}",
    "v1/owner/profile/{owner_id}",
    "v1/pvp_girl/{girl_mid}",
    "v1/radio_station/bgm/{scene_mid}",
    "v1/ranking/border/{ranking_id}",
    "v1/ranking/finalresult/{ranking_id}",
    "v1/ranking/score/{ranking_id}",
    "v1/shop/exchange/{product_mid}",
    "v1/swimsuit_arrange_flag/{owner_id}",
    "v1/tutorial/{event_mid}",
)


@functools.cache
def get_json_dir() -> Path:
    return config.DATA_DIR / "json" / "api"


@functools.cache
def get_schema_dir() -> Path:
    return config.DATA_DIR / "schema" / "api"


@functools.cache
def get_model_dir() -> Path:
    return config.DATA_DIR / "model" / "api"


def is_valid_message(request: Request, message: Message) -> bool:
    return bool(
        request.pretty_host == "api.doaxvv.com"
        and "X-DOAXVV-Encrypted" in message.headers
        and message.content
    )


def iter_messages(flow: HTTPFlow) -> Iterable[Message]:
    for message in (flow.request, flow.response):
        if is_valid_message(flow.request, message):
            yield message


def get_fernet(password: str) -> Fernet:
    return Fernet(base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest()))


def decrypt_message(key: str, message: Message) -> bytes:
    decrypted_data = utils.decrypt_data(
        AES(get_fernet(key).decrypt(message.headers["Proxy-X-DOAXVV-Encrypted"])),
        message.content,
        base64.b64decode(message.headers["X-DOAXVV-Encrypted"]),
    )
    uncompressed_data = zlib.decompress(decrypted_data)
    return uncompressed_data


def flows_to_json(path: Path):
    logging.info(f"[FLOWS] {path}")

    with path.open("rb") as file:
        flow_reader = FlowReader(file)
        for flow in flow_reader.stream():
            flow: HTTPFlow
            logging.debug(f"[FLOW] {flow.id}")

            for message in iter_messages(flow):
                json_data = decrypt_message(flow.id, message)

                relative_path = flow.request.path.removeprefix("/")
                path_method = flow.request.method.lower()
                path_message = type(message).__name__.lower()
                path_name = f"{path.stem}-{flow.id}.json"
                json_path = (
                    get_json_dir()
                    / relative_path
                    / path_method
                    / path_message
                    / path_name
                )
                logging.warning(f"[JSON] {json_path}")

                json_path.parent.mkdir(parents=True, exist_ok=True)
                json_path.write_bytes(json_data)


def aggregate_json(path: str):
    formatter = Formatter()
    variables = {parse_result[1] for parse_result in formatter.parse(path)}
    variable_path = str(get_json_dir() / path)
    variable_path_dst = variable_path.format(
        **{variable: f"_{variable}_" for variable in variables}
    )
    for variable_path_src in glob.iglob(
        variable_path.format(**{variable: "[0-9]*" for variable in variables})
    ):
        src_path = Path(variable_path_src)
        for json_path in src_path.rglob("*.json"):
            json_path: Path
            relative_path = json_path.relative_to(src_path)
            dst_path = variable_path_dst / relative_path
            dst_path.parent.mkdir(parents=True, exist_ok=True)
            json_path.rename(dst_path)


def rmtree_empty(path: Path):
    for child in path.iterdir():
        if child.is_dir():
            rmtree_empty(child)
    if not any(path.iterdir()):
        path.rmdir()


def to_model():
    shutil.rmtree(get_json_dir(), True)
    for flows_path in (config.DATA_DIR / "flows").glob("*.flows"):
        if flows_path.is_file():
            flows_to_json(flows_path)

    for variable_path in VARIABLE_PATHS:
        aggregate_json(variable_path)
    rmtree_empty(get_json_dir())

    shutil.rmtree(get_schema_dir(), True)
    path_paths = set()
    for json_path in (get_json_dir()).rglob("*.json"):
        if json_path.is_file():
            path_paths.add(json_path.parent)
    for path_path in path_paths:
        utils.json_to_schema(path_path, get_json_dir(), get_schema_dir())

    shutil.rmtree(get_model_dir(), True)
    for schema_path in (get_schema_dir()).rglob("*.schema.json"):
        if schema_path.is_file():
            utils.schema_to_model(schema_path, get_schema_dir(), get_model_dir())

    base_path = get_model_dir()
    path_paths = set()
    for model_path in base_path.rglob("*.py"):
        model_path: Path
        if model_path.is_file():
            path_path = model_path.relative_to(base_path).parent.parent
            for part in path_path.parts:
                if part.isdigit():
                    path_paths.add(path_path)
                    break
    for path_path in sorted(path_paths):
        logging.error(path_path.as_posix())
