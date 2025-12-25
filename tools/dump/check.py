import logging
from pathlib import Path
from shutil import COPY_BUFSIZE

from httpx import URL
from httpx import Client

from . import config
from . import utils

logger = logging.getLogger(__name__)


def remove_paths(data_dir: Path, client: Client) -> None:
    for path in data_dir.rglob("*"):
        if not path.is_file():
            continue

        logger.debug("[PATH] %s", path)
        relative_path = path.relative_to(data_dir)

        response = client.head(relative_path.as_posix())
        response.raise_for_status()
        md5 = utils.etag_pattern.match(response.headers["ETag"]).group("md5")

        if not utils.check_md5(path, md5):
            logger.error("[PATH] %s", path)
            path.unlink()

    utils.rmtree_empty(data_dir)


def main() -> None:
    remove_paths(config.DATA_DIR / "game", Client(base_url=URL(scheme="https", host="game.doaxvv.com")))
    remove_paths(config.DATA_DIR / "cdn01", Client(base_url=URL(scheme="https", host="cdn01.doax-venusvacation.jp")))


if __name__ == "__main__":
    main()
