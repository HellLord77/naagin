import hashlib
import json
import logging
import shutil
from pathlib import Path

from httpx import Client
from httpx import URL

import config
import csv_
import flow
from naagin.enums import ItemConsumeTypeEnum


def consume_to_enum():
    path = (
        config.DATA_DIR
        / "schema"
        / "api"
        / "v1"
        / "item"
        / "consume"
        / "get"
        / "response.schema.json"
    )
    with path.open("rb") as file:
        json_data = json.load(file)
    examples = json_data["examples"]
    types = set()
    for example in examples:
        for item_consume in example["item_consume_list"]:
            type_ = item_consume["type"]
            types.add(type_)
    for type_ in sorted(types):
        if type_ in ItemConsumeTypeEnum:
            item_consume_type = ItemConsumeTypeEnum(type_)
            print(f"{item_consume_type.name} = {type_}")
        else:
            print(f"_VALUE_{type_} = {type_}")


def get_md5(path: Path) -> str:
    md5 = hashlib.md5()
    with path.open("rb") as file:
        while chunk := file.read(shutil.COPY_BUFSIZE):
            md5.update(chunk)
    return md5.hexdigest()


def game_to_tmp():
    game_dir = config.DATA_DIR / "game"
    temp_dir = config.DATA_DIR / "temp"
    client = Client(base_url=URL(scheme="https", host="game.doaxvv.com"))

    for path in game_dir.rglob("*[!.temp]"):
        path: Path
        if path.is_file():
            logging.warning("[GAME] %s", path)

            relative_path = path.relative_to(game_dir)

            response = client.head(relative_path.as_posix())
            response.raise_for_status()
            etag = response.headers["ETag"][1:-1]
            hash_, _ = etag.split(":")

            if hash_ != get_md5(path):
                logging.error(path)

                temp_path = (temp_dir / relative_path).with_suffix(".temp")
                temp_path.parent.mkdir(parents=True, exist_ok=True)
                path.rename(temp_path)


def main():
    if config.FLOW:
        flow.to_model()

    if config.CSV:
        csv_.to_model()

    if config.GAME:
        game_to_tmp()

    # consume_to_enum()


if __name__ == "__main__":
    main()
