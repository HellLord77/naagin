import base64
import hashlib
import json
import logging
from http import HTTPMethod
from pathlib import Path
from typing import Any

import httpx
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from httpx import URL
from httpx import Client

from . import config
from . import utils

logger = logging.getLogger(__name__)


def write_resource(path: Path, json_data: dict[str, Any]) -> None:
    logger.warning("[WRITE] %s", path)
    path.parent.mkdir(parents=True, exist_ok=True)
    data = json.dumps(json_data, indent=2)
    path.write_text(data)


def decrypt_resource_data(platform_id: int, key: bytes, encrypted_data: str) -> bytes:
    md5 = hashlib.md5(key, usedforsecurity=False)
    encoded_key = md5.hexdigest().encode()
    decoded_data = base64.b64decode(encrypted_data)
    md5.update(str(platform_id).encode())
    initialization_vector = md5.digest()
    return utils.decrypt_data(AES(encoded_key), decoded_data, initialization_vector)


def download_resource_list() -> None:
    response = httpx.get("https://api01.doaxvv.com/v1/resource/list")
    response.raise_for_status()
    resource_list = response.json()

    path = (
        config.DATA_DIR
        / "api01"
        / "v1"
        / "resource"
        / "list"
        / f"{resource_list['resource_list']['exe'][0]['version']}.json"
    )
    write_resource(path, resource_list)


def download_resource_list_jp() -> None:
    platform_id = 0
    response = httpx.get(f"https://api01.doax-venusvacation.jp/v1/resource/key/{platform_id}")
    response.raise_for_status()
    encrypted_key = response.json()

    key = decrypt_resource_data(platform_id, encrypted_key["p"].encode(), encrypted_key["e"]).decode()
    response = httpx.post(
        "https://api01.doax-venusvacation.jp/v1/resource/list/encrypt", json={"key": key, "platform_id": platform_id}
    )
    response.raise_for_status()
    encrypted_resource_list = response.json()

    resource_list = json.loads(
        decrypt_resource_data(
            platform_id, encrypted_resource_list["p"].encode(), encrypted_resource_list["resource_list_encrypt"]
        )
    )
    path = (
        config.DATA_DIR
        / "api01"
        / "v1"
        / "resource"
        / "list"
        / "encrypt"
        / f"{resource_list['resource_list']['exe'][0]['version']}.json"
    )
    write_resource(path, resource_list)


def resources_to_app(app: str, client: Client, resources: list[dict[str, Any]], patch_type: str) -> None:
    for resource in resources:
        directory = resource["directory"]
        name = resource["file_name"]
        path = config.DATA_DIR / app / "production" / "patch_data" / patch_type / directory / name

        if (
            not path.is_file()
            or resource["file_size"] != path.stat().st_size
            or resource["hash"] != utils.get_md5(path)
        ):
            logger.warning("[DOWNLOAD] %s", path)
            with client.stream(HTTPMethod.GET, f"/production/patch_data/{patch_type}/{directory}/{name}") as response:
                response.raise_for_status()
                path.parent.mkdir(parents=True, exist_ok=True)

                with path.open("wb") as file:
                    for chunk in response.iter_bytes():
                        file.write(chunk)


def json_to_resources(app: str, client: Client, json_path: Path) -> None:
    logger.info("[JSON] %s", json_path)

    with json_path.open("rb") as file:
        resource_list = json.load(file)

    resource_file_list = resource_list["resource_list"]
    resources_to_app(app, client, resource_file_list.pop("exe"), "app")
    for resources in resource_file_list.values():
        resources_to_app(app, client, resources, "resource")


def download_patch_data(app: str, host: str, directory: str) -> None:
    client = Client(base_url=URL(scheme="https", host=host))
    src_path = config.DATA_DIR / "api01" / "v1" / "resource" / "list" / directory

    for json_path in src_path.glob("*.json"):
        json_to_resources(app, client, json_path)


def download_csv(app: str, host: str, master_version: int, application_version: int) -> None:
    csv_list_path = (
        config.DATA_DIR / "api" / "v1" / "csv" / "list" / str(master_version) / f"{application_version}.json"
    )
    with csv_list_path.open("rb") as file:
        csv_list = json.load(file)

    csv_file_list = csv_list["csv_file_list"]
    del csv_file_list["file_encrypt_key"]

    client = Client(base_url=URL(scheme="https", host=host))
    src_path = config.DATA_DIR / app / "production" / "csv" / str(master_version)

    for initialization_vector in csv_file_list.values():
        encrypted_path = src_path / initialization_vector
        if not encrypted_path.is_file():
            logger.warning("[DOWNLOAD] %s", encrypted_path)
            response = client.get(f"/production/csv/{master_version}/{initialization_vector}")
            response.raise_for_status()

            encrypted_path.parent.mkdir(parents=True, exist_ok=True)
            encrypted_path.write_bytes(response.content)


def main() -> None:
    download_resource_list()
    download_resource_list_jp()

    download_patch_data("game", "game.doaxvv.com", "")
    download_patch_data("cdn01", "cdn01.doax-venusvacation.jp", "encrypt")

    download_csv("game", "game.doaxvv.com", config.MASTER_VERSION, config.APPLICATION_VERSION)
    download_csv("cdn01", "cdn01.doax-venusvacation.jp", config.MASTER_VERSION_JP, config.APPLICATION_VERSION_JP)


if __name__ == "__main__":
    main()
