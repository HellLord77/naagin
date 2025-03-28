import hashlib
import logging
import shutil
from pathlib import Path

from httpx import URL
from httpx import Client

import config
import utils


def get_md5(path: Path) -> str:
    md5 = hashlib.md5()
    with path.open("rb") as file:
        while chunk := file.read(shutil.COPY_BUFSIZE):
            md5.update(chunk)
    return md5.hexdigest()


def to_tmp():
    game_dir = config.DATA_DIR / "game"
    client = Client(base_url=URL(scheme="https", host="game.doaxvv.com"))

    for path in game_dir.rglob("*"):
        path: Path
        if not path.is_file():
            continue

        logging.warning("[GAME] %s", path)
        relative_path = path.relative_to(game_dir)

        response = client.head(relative_path.as_posix())
        response.raise_for_status()
        hash_ = response.headers["ETag"][1:33]

        if hash_ != get_md5(path):
            logging.error(path)
            path.unlink()

    utils.rmtree_empty(game_dir)
