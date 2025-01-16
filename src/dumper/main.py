import hashlib
import logging
import shutil
from pathlib import Path

from httpx import Client
from httpx import URL

import config
import csv_
import flows


def get_md5(path: Path) -> str:
    md5 = hashlib.md5()
    with path.open("rb") as file:
        while chunk := file.read(shutil.COPY_BUFSIZE):
            md5.update(chunk)
    return md5.hexdigest()


def game_to_tmp():
    base_path = config.DATA_DIR / "game"
    client = Client(base_url=URL(scheme="https", host="game.doaxvv.com"))

    for path in base_path.rglob("*[!.tmp]"):
        path: Path
        if path.is_file():
            logging.warning("[GAME] %s", path)

            relative_path = path.relative_to(base_path)

            response = client.head(relative_path.as_posix())
            response.raise_for_status()
            etag = response.headers["ETag"][1:-1]
            hash_, _ = etag.split(":")

            if hash_ != get_md5(path):
                logging.error(path)

                path.rename(path.with_suffix(".tmp"))


def main():
    # logging.basicConfig(level=logging.CRITICAL)

    flows.to_model()
    exit()

    csv_.to_model()
    exit()

    game_to_tmp()
    exit()


if __name__ == "__main__":
    main()
