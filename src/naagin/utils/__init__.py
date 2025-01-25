from typing import Any
from zlib import decompress

from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import CBC
from cryptography.hazmat.primitives.padding import PKCS7
from fastapi import Request
from fastapi import Response
from starlette.datastructures import MutableHeaders
from starlette.types import Scope

from naagin.utils.encoder import DeflateEncoder
from .doaxvv_header import DOAXVVHeader


def get_route_path(scope: Scope) -> str:
    path = scope["path"]
    root_path = scope.get("root_path", "")
    return path.removeprefix(root_path)


def should_endec(scope: Scope) -> bool:
    route_path = get_route_path(scope)
    return route_path.startswith("/api/") and not route_path.startswith(
        "/api/v1/session"
    )


def decrypt_data(data: bytes, key: bytes, initialization_vector: bytes) -> bytes:
    algorithm = AES(key)
    mode = CBC(initialization_vector)
    decryptor = Cipher(algorithm, mode).decryptor()
    encrypted = decryptor.update(data) + decryptor.finalize()

    unpadder = PKCS7(AES.block_size).unpadder()
    unpadded = unpadder.update(encrypted) + unpadder.finalize()
    return unpadded


def request_set_header(self: Request, key: str, value: Any):
    headers = self.headers
    if not isinstance(self.headers, MutableHeaders):
        headers = self.headers.mutablecopy()
        self._headers = headers
    headers[key] = str(value)


async def request_decrypt_body(self: Request, key: bytes, initialization_vector: bytes):
    body = await self.body()
    body = decrypt_data(body, key, initialization_vector)

    request_set_header(self, "Content-Length", len(body))
    self._body = body


async def request_decompress_body(self: Request):
    body = await self.body()
    body = decompress(body)

    request_set_header(self, "Content-Length", len(body))
    self._body = body


def response_set_doaxvv_header(self: Response, alias: str, value: Any):
    key = DOAXVVHeader(alias)
    self.headers[key] = str(value)
