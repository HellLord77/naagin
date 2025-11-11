import hashlib
import logging
from pathlib import Path
from shutil import COPY_BUFSIZE

from httpx import URL
from httpx import Client

from . import config
from . import utils

logger = logging.getLogger(__name__)


def get_md5(path: Path) -> str:
    md5 = hashlib.md5()  # noqa: S324
    with path.open("rb") as file:
        while chunk := file.read(COPY_BUFSIZE):
            md5.update(chunk)
    return md5.hexdigest()


def to_tmp() -> None:
    game_dir = config.DATA_DIR / "game"
    client = Client(base_url=URL(scheme="https", host="game.doaxvv.com"))

    for path in game_dir.rglob("*"):
        if not path.is_file():
            continue

        logger.warning("[GAME] %s", path)
        relative_path = path.relative_to(game_dir)

        response = client.head(relative_path.as_posix())
        response.raise_for_status()
        md5 = response.headers["ETag"][1:33]

        if md5 != get_md5(path):
            logger.error(path)
            path.unlink()

    utils.rmtree_empty(game_dir)


if __name__ == "__main__":
    to_tmp()
