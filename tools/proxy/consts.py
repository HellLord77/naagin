import atexit
import time
import urllib.parse
from pathlib import Path

import config
from mitmproxy.io import FlowWriter

API_HOST = "api.doaxvv.com"
API_JP_HOST = "api.doax-venusvacation.jp"
API01_HOST = "api01.doaxvv.com"
API01_JP_HOST = "api01.doax-venusvacation.jp"
GAME_HOST = "game.doaxvv.com"
CDN01_HOST = "cdn01.doax-venusvacation.jp"
WWW_HOST = "doax-venusvacation.jp"

API_HOSTS = {API_HOST, API_JP_HOST}
API_01_HOSTS = {API01_HOST, API01_JP_HOST}
RES_HOSTS = {GAME_HOST, CDN01_HOST, WWW_HOST}
RESP_PATHS = {GAME_HOST: "game", CDN01_HOST: "cdn01", WWW_HOST: "www"}

SERVER_URL = urllib.parse.urlparse(config.SERVER_URL)
CERT_DIR = config.DATA_DIR / "cert"

if config.WRITE_FILE:
    FLOW_WRITER = FlowWriter((config.DATA_DIR / "flows" / f"DOAXVV-{int(time.time())}.flows").open("wb"))

    def _close_file() -> None:
        file = FLOW_WRITER.fo
        size = file.tell()
        file.close()

        if size == 0:
            Path.unlink(file.name)

    atexit.register(_close_file)
