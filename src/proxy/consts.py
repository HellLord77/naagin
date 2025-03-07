import time
import urllib.parse

from mitmproxy.io import FlowWriter

import config

API_HOST = "api.doaxvv.com"
API01_HOST = "api01.doaxvv.com"
GAME_HOST = "game.doaxvv.com"

SERVER_URL = urllib.parse.urlparse(config.SERVER_URL)

CERT_DIR = config.DATA_DIR / "cert"

if config.WRITE_FILE:
    FLOW_WRITER = FlowWriter(
        (config.DATA_DIR / "flows" / f"DOAXVV-{int(time.time())}.flows").open("wb")
    )
