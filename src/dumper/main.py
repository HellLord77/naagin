import glob
import json
import logging
import shutil
from datetime import datetime
from pathlib import Path
from string import Formatter
from typing import Any
from typing import Iterable

import frozendict
from datamodel_code_generator.parser.jsonschema import JsonSchemaParser
from genson import SchemaBuilder
from genson import TypedSchemaStrategy
from mitmproxy.http import HTTPFlow
from mitmproxy.http import Message
from mitmproxy.io import FlowReader

import config
import utils

VARIABLE_PATHS = (
    "v1/dishevelment/{owner_id}/{item_mid}",
    "v1/girl/{girl_mid}",
    "v1/item/consume/use/{item_mid}",
    "v1/item/equipment/type/{type}",
    "v1/max_combine/{owner_id}/{item_mid}",
    "v1/onsen/{onsen_mid}/item/use/{item_mid}",
    "v1/onsen/{onsen_mid}/reward",
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


def iter_messages(flow: HTTPFlow) -> Iterable[Message]:
    for message in (flow.request, flow.response):
        if utils.is_valid_message(flow.request, message.content):
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
                    config.DATA_DIR
                    / "json"
                    / relative_path
                    / path_method
                    / path_message
                    / path_name
                )
                logging.warning(f"[JSON] {json_path}")

                json_path.parent.mkdir(parents=True, exist_ok=True)
                json_path.write_bytes(json_data)


class AbstractDateTime(TypedSchemaStrategy):
    FORMAT_STRING: str
    FORMAT_NAME: str

    JS_TYPE = "string"
    PYTHON_TYPE = (str,)

    @classmethod
    def match_schema(cls, schema: dict) -> bool:
        return super().match_schema(schema) and schema.get("format") == cls.FORMAT_NAME

    @classmethod
    def match_object(cls, obj: Any) -> bool:
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


def json_to_schema(path: Path):
    logging.info(f"[PATH] {path}")

    data_hashes = set()
    json_datas = []
    schema_builder = CustomSchemaBuilder()
    for json_path in path.rglob("*.json"):
        json_path: Path
        logging.debug(f"[JSON] {json_path}")

        with json_path.open("rb") as file:
            json_data = json.load(file)
        data_hash = frozendict.deepfreeze(json_data, {list: frozenset})
        if data_hash not in data_hashes:
            data_hashes.add(data_hash)
            json_datas.append(json_data)
            schema_builder.add_object(json_data)

    relative_path = path.relative_to(config.DATA_DIR / "json")

    schema = schema_builder.to_schema()
    schema["title"] = "_".join(relative_path.parts[1:])
    schema["examples"] = json_datas

    schema_path = config.DATA_DIR / "schema" / relative_path.with_suffix(".schema.json")
    logging.warning(f"[SCHEMA] {schema_path}")

    schema_path.parent.mkdir(parents=True, exist_ok=True)
    with schema_path.open("w") as file:
        # noinspection PyTypeChecker
        json.dump(schema, file, separators=(",", ":"))


def custom_class_name_generator(title: str):
    return f"{title.removesuffix("_list")}_model"


def schema_to_model(path: Path):  # TODO datetime, date, time serializer
    logging.info(f"[SCHEMA] {path}")

    schema_data = path.read_text()
    parser = JsonSchemaParser(
        schema_data,
        use_standard_collections=True,
        use_title_as_name=True,
        disable_appending_item_suffix=True,
        custom_class_name_generator=custom_class_name_generator,
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

    relative_path = path.relative_to(config.DATA_DIR / "schema").with_suffix("")
    model_path = config.DATA_DIR / "model" / relative_path.with_suffix(".py")
    logging.warning(f"[MODEL] {model_path}")

    model_path.parent.mkdir(parents=True, exist_ok=True)
    model_path.write_text(model_data, "utf-8")


def rmtree_empty(path: Path):
    for child in path.iterdir():
        if child.is_dir():
            rmtree_empty(child)
    if not any(path.iterdir()):
        path.rmdir()


def main():
    # logging.basicConfig(level=logging.CRITICAL)

    shutil.rmtree(config.DATA_DIR / "json", True)

    for flows_path in (config.DATA_DIR / "flows").glob("*.flows"):
        if flows_path.is_file():
            flows_to_json(flows_path)

    formatter = Formatter()
    for variable_path in VARIABLE_PATHS:
        variables = {parse_result[1] for parse_result in formatter.parse(variable_path)}
        variable_path_template = str(config.DATA_DIR / "json" / variable_path)
        variable_path_dst = variable_path_template.format(
            **{variable: f"_{variable}_" for variable in variables}
        )
        for variable_path_src in glob.iglob(
            variable_path_template.format(
                **{variable: "[0-9]*" for variable in variables}
            )
        ):
            src_path = Path(variable_path_src)
            for json_path in src_path.rglob("*.json"):
                json_path: Path
                relative_path = json_path.relative_to(src_path)
                dst_path = variable_path_dst / relative_path
                dst_path.parent.mkdir(parents=True, exist_ok=True)
                json_path.rename(dst_path)
    rmtree_empty(config.DATA_DIR / "json")

    shutil.rmtree(config.DATA_DIR / "schema", True)

    path_paths = set()
    for json_path in (config.DATA_DIR / "json").rglob("*.json"):
        if json_path.is_file():
            path_paths.add(json_path.parent)
    for path_path in path_paths:
        json_to_schema(path_path)

    shutil.rmtree(config.DATA_DIR / "model", True)

    for schema_path in (config.DATA_DIR / "schema").rglob("*.schema.json"):
        if schema_path.is_file():
            schema_to_model(schema_path)

    base_path = config.DATA_DIR / "model"
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


if __name__ == "__main__":
    main()
