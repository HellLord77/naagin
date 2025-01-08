import json
import logging
import shutil
from pathlib import Path
from typing import Iterable

from datamodel_code_generator.parser.jsonschema import JsonSchemaParser
from genson import SchemaBuilder
from mitmproxy.http import HTTPFlow
from mitmproxy.http import Message
from mitmproxy.io import FlowReader

import config
import utils


def class_name_generator(title: str):
    return f"{title.removesuffix("_list")}_model"


def iter_messages(flow: HTTPFlow) -> Iterable[Message]:
    for message in (flow.request, flow.response):
        if utils.is_valid_message(flow.request, message.content):
            yield message


def flows_to_json(path: Path):
    logging.info(f"[FLOWS] {path}")

    with path.open("rb") as file:
        reader = FlowReader(file)
        for flow in reader.stream():
            flow: HTTPFlow
            logging.debug(f"[FLOW] {flow.id}")

            for message in iter_messages(flow):
                json_data = utils.decrypt_message(flow.id, message)

                relative_path = flow.request.path.removeprefix("/")
                path_method = flow.request.method.lower()
                path_message = type(message).__name__.lower()
                path_flow = path.stem
                path_name = f"{flow.id}.json"
                json_path = (
                    config.DATA_DIR
                    / "json"
                    / relative_path
                    / path_method
                    / path_message
                    / path_flow
                    / path_name
                )
                logging.warning(f"[JSON] {json_path}")

                json_path.parent.mkdir(parents=True, exist_ok=True)
                json_path.write_bytes(json_data)


def json_to_schema(path: Path):
    logging.info(f"[PATH] {path}")

    datas = set()
    for json_path in path.rglob("*.json"):
        json_path: Path
        logging.debug(f"[JSON] {json_path}")

        data = json_path.read_bytes()
        datas.add(data)

    examples = []
    builder = SchemaBuilder()
    for data in datas:
        json_data = json.loads(data)
        examples.append(json_data)
        builder.add_object(json_data)

    relative_path = path.relative_to(config.DATA_DIR / "json")

    schema = builder.to_schema()
    schema["title"] = "_".join(relative_path.parts[1:])
    schema["examples"] = examples

    schema_path = config.DATA_DIR / "schema" / relative_path.with_suffix(".schema.json")
    logging.warning(f"[SCHEMA] {schema_path}")

    schema_path.parent.mkdir(parents=True, exist_ok=True)
    with schema_path.open("w") as file:
        # noinspection PyTypeChecker
        json.dump(schema, file, separators=(",", ":"))


def schema_to_model(path: Path):
    logging.info(f"[SCHEMA] {path}")

    data = path.read_text()
    parser = JsonSchemaParser(
        data,
        use_standard_collections=True,
        use_title_as_name=True,
        disable_appending_item_suffix=True,
        custom_class_name_generator=class_name_generator,
    )
    parsed_data = parser.parse()
    parsed_lines = parsed_data.split("\n")[2:]

    if config.EXAMPLES:
        parsed_lines.insert(0, "from pydantic import ConfigDict")
        json_data = json.loads(data)
        examples = json_data["examples"]
        json_schema_extra = {"examples": examples}
        parsed_lines.append(
            f"    model_config = ConfigDict(json_schema_extra={json_schema_extra})"
        )
        parsed_lines.append("")
    model_data = "\n".join(parsed_lines)

    relative_path = path.relative_to(config.DATA_DIR / "schema").with_suffix("")
    model_path = config.DATA_DIR / "model" / relative_path.with_suffix(".py")
    logging.warning(f"[MODEL] {model_path}")

    model_path.parent.mkdir(parents=True, exist_ok=True)
    model_path.write_text(model_data, "utf-8")


def main():
    shutil.rmtree(config.DATA_DIR / "json", True)

    for flows_path in (config.DATA_DIR / "flows").glob("*.flows"):
        if flows_path.is_file():
            flows_to_json(flows_path)

    shutil.rmtree(config.DATA_DIR / "schema", True)

    path_paths = set()
    for json_path in (config.DATA_DIR / "json").rglob(
        "*.json"
    ):  # TODO path.parts[].isdigit()
        if json_path.is_file():
            path_paths.add(json_path.parent.parent)
    for path_path in path_paths:
        json_to_schema(path_path)

    shutil.rmtree(config.DATA_DIR / "model", True)

    for schema_path in (config.DATA_DIR / "schema").rglob("*.schema.json"):
        if schema_path.is_file():
            schema_to_model(schema_path)


if __name__ == "__main__":
    main()
