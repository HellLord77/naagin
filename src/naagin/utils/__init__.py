from typing import Any
from zlib import decompress

from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import CBC
from cryptography.hazmat.primitives.padding import PKCS7
from fastapi import Request
from fastapi import Response
from starlette.types import Scope

from .case_sensitive_header import CaseSensitiveHeader


def get_route_path(scope: Scope) -> str:
    path = scope["path"]
    root_path = scope.get("root_path", "")
    return path.removeprefix(root_path)


def should_endec(scope: Scope) -> bool:
    route_path = get_route_path(scope)
    return not route_path.startswith("/v1/session")


def decrypt_data(data: bytes, key: bytes, initialization_vector: bytes) -> bytes:
    algorithm = AES(key)
    mode = CBC(initialization_vector)
    decryptor = Cipher(algorithm, mode).decryptor()
    encrypted = decryptor.update(data) + decryptor.finalize()

    unpadder = PKCS7(AES.block_size).unpadder()
    unpadded = unpadder.update(encrypted) + unpadder.finalize()
    return unpadded


async def request_decrypt_body(self: Request, key: bytes, initialization_vector: bytes):
    body = await self.body()
    body = decrypt_data(body, key, initialization_vector)

    headers = self.headers.mutablecopy()
    headers["Content-Type"] = "application/json"
    headers["Content-Length"] = str(len(body))

    self._headers = headers
    self._body = body


async def request_decompress_body(self: Request):
    body = await self.body()
    body = decompress(body)

    headers = self.headers.mutablecopy()
    headers["Content-Length"] = str(len(body))

    self._headers = headers
    self._body = decompress(body)


def response_set_doaxvv_header(self: Response, key: str, value: Any):
    alias = CaseSensitiveHeader(f"X-DOAXVV-{key}")
    self.headers[alias] = str(value)
