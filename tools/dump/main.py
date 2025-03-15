import base64
import hashlib
import logging

from cryptography.fernet import Fernet
from mitmproxy.http import HTTPFlow
from mitmproxy.io import FlowReader
from mitmproxy.io import FlowWriter

import config
import csv_
import flow
import game
import utils


def get_fernet(password: str) -> Fernet:
    return Fernet(base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest()))


def convert_flow():
    temp_dir = config.DATA_DIR / "temp"

    for flows_path in (config.DATA_DIR / "flows").glob("*.flows"):
        with flows_path.open("rb") as file:
            flow_reader = FlowReader(file)

            temp_path = temp_dir / flows_path.name
            with temp_path.open("wb") as file_:
                flow_writer = FlowWriter(file_)

                for flow_ in flow_reader.stream():
                    flow_: HTTPFlow
                    logging.debug(f"[FLOW] {flow_.id}")

                    for message in utils.iter_messages(flow_):
                        if not flow_.comment:
                            key = get_fernet(flow_.id).decrypt(
                                message.headers["Proxy-X-DOAXVV-Encrypted"]
                            )
                            flow_.comment = base64.b64encode(key).decode()

                        del message.headers["Proxy-X-DOAXVV-Encrypted"]
                    flow_writer.add(flow_)


def main():
    convert_flow()
    exit()

    if config.FLOW:
        flow.to_model()

    if config.CSV:
        csv_.to_model()

    if config.GAME:
        game.to_tmp()


if __name__ == "__main__":
    main()
