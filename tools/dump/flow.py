import functools
import glob
import logging
import operator
import shutil
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from string import Formatter
from typing import Generator

from mitmproxy.http import HTTPFlow
from mitmproxy.http import Message
from mitmproxy.io import FlowReader

import config
import utils

VARIABLE_PATHS = [
    "v1/dishevelment/{owner_id}/{item_mid}",
    "v1/friendship/friend_code/{friend_code}",
    "v1/friendship/{owner_id}",
    "v1/furniture/layout/{set_no}",
    "v1/furniture/myset/{owner_id}/list",
    "v1/girl/private/favorite/{type}",
    "v1/girl/{girl_mid}",
    "v1/girl/{girl_mid}/head/accessory/switch/{owner_id}",
    "v1/girl/{girl_mid}/private/favorite/{type}",
    "v1/item/consume/use/{item_mid}",
    "v1/item/equipment/type/{type}",
    "v1/max_combine/{owner_id}/{item_mid}",
    "v1/onsen/{onsen_mid}/entry/slot",
    "v1/onsen/{onsen_mid}/item/use/{item_mid}",
    "v1/onsen/{onsen_mid}/reward",
    "v1/onsen/{onsen_mid}/update/quality",
    "v1/owner/detail/{owner_id}",
    "v1/owner/episode/exchange/{episode_mid}",
    "v1/owner/episode/{episode_mid}",
    "v1/owner/profile/{owner_id}",
    "v1/pvp_girl/{girl_mid}",
    "v1/radio_station/bgm/{scene_mid}",
    "v1/ranking/border/{ranking_id}",
    "v1/ranking/finalresult/{ranking_id}",
    "v1/ranking/score/{ranking_id}",
    "v1/room/detail/{owner_id}",
    "v1/seal/{girl_mid}",
    "v1/shop/exchange/{product_mid}",
    "v1/swimsuit_arrange_flag/{owner_id}",
    "v1/tutorial/{event_mid}",
]


@functools.cache
def get_json_dir() -> Path:
    return config.DATA_DIR / "json" / "api"


@functools.cache
def get_schema_dir() -> Path:
    return config.DATA_DIR / "schema" / "api"


@functools.cache
def get_model_dir() -> Path:
    return config.DATA_DIR / "model" / "api"


def iter_messages(flow: HTTPFlow) -> Generator[Message]:
    for message in (flow.request, flow.response):
        if utils.is_valid_message(flow.request, message):
            yield message


def flows_to_json(path: Path):
    logging.info(f"[FLOWS] {path}")

    with path.open("rb") as file:
        flow_reader = FlowReader(file)
        for flow in flow_reader.stream():
            flow: HTTPFlow
            logging.debug(f"[FLOW] {flow.id}")

            for message in iter_messages(flow):
                json_data = utils.decrypt_message(flow.id, message)

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
        **{variable: f"__{variable}__" for variable in variables}
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

    VARIABLE_PATHS.sort(reverse=True)
    for variable_path in VARIABLE_PATHS:
        aggregate_json(variable_path)
    rmtree_empty(get_json_dir())

    shutil.rmtree(get_schema_dir(), True)
    json_to_schema = functools.partial(
        utils.json_to_schema, json_dir=get_json_dir(), schema_dir=get_schema_dir()
    )
    json_dirs = set(
        map(
            operator.attrgetter("parent"),
            filter(Path.is_file, get_json_dir().rglob("*.json")),
        )
    )
    with ThreadPoolExecutor() as executor:
        utils.consume(executor.map(json_to_schema, json_dirs))

    shutil.rmtree(get_model_dir(), True)
    schema_to_model = functools.partial(
        utils.schema_to_model, schema_dir=get_schema_dir(), model_dir=get_model_dir()
    )
    schema_paths = filter(Path.is_file, get_schema_dir().rglob("*.schema.json"))
    with ProcessPoolExecutor() as executor:
        utils.consume(executor.map(schema_to_model, schema_paths))

    utils.model_formatter(get_model_dir())

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
