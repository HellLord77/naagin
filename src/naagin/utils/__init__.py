from base64 import b64encode
from secrets import token_bytes
from typing import Any
from typing import AsyncGenerator
from typing import AsyncIterable
from typing import MutableMapping
from zlib import compressobj
from zlib import decompress

from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import CBC
from cryptography.hazmat.primitives.padding import PKCS7
from fastapi import Request
from fastapi.datastructures import Headers
from fastapi.responses import StreamingResponse

from naagin.enums import EncodingEnum
from .doaxvv_header import DOAXVVHeader


def get_route_path(scope: dict[str, Any]) -> str:
    path = scope["path"]
    root_path = scope.get("root_path", "")
    return path.removeprefix(root_path)


def should_endec(scope: dict[str, Any]) -> bool:
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


async def iter_compress_data(
    data_stream: AsyncIterable[bytes],
) -> AsyncGenerator[bytes]:
    compressor = compressobj()
    async for data in data_stream:
        yield compressor.compress(data)
    yield compressor.flush()


async def iter_encrypt_data(
    data_stream: AsyncIterable[bytes], key: bytes, initialization_vector: bytes
) -> AsyncGenerator[bytes]:
    padder = PKCS7(AES.block_size).padder()
    encryptor = Cipher(AES(key), CBC(initialization_vector)).encryptor()
    async for data in data_stream:
        yield encryptor.update(padder.update(data))
    yield encryptor.update(padder.finalize())
    yield encryptor.finalize()


def request_header(self: Request) -> MutableMapping[str, str]:
    headers = self.headers
    if type(self.headers) is Headers:
        headers = self.headers.mutablecopy()
        self._headers = headers
    return headers


def request_set_header(self: Request, key: str, value: Any):
    headers = request_header(self)
    headers[key] = str(value)


def request_del_header(self: Request, key: str):
    headers = request_header(self)
    del headers[key]


async def request_decrypt_body(self: Request, key: bytes, initialization_vector: bytes):
    body = await self.body()
    body = decrypt_data(body, key, initialization_vector)

    request_set_header(self, "Content-Length", len(body))
    request_del_header(self, "X-DOAXVV-Encrypted")
    self._body = body


async def request_decompress_body(self: Request):
    body = await self.body()
    body = decompress(body)

    request_set_header(self, "Content-Length", len(body))
    request_del_header(self, "X-DOAXVV-Encoding")
    self._body = body


def response_compress_body(self: StreamingResponse):
    del self.headers["Content-Length"]
    self.headers["Content-Type"] = "application/octet-stream"
    DOAXVVHeader.set(self, "Encoding", EncodingEnum.DEFLATE)
    self.body_iterator = iter_compress_data(self.body_iterator)


def response_encrypt_body(self: StreamingResponse, key: bytes):
    initialization_vector = token_bytes(16)
    del self.headers["Content-Length"]
    self.headers["Content-Type"] = "application/octet-stream"
    DOAXVVHeader.set(self, "Encrypted", b64encode(initialization_vector).decode())
    self.body_iterator = iter_encrypt_data(
        self.body_iterator, key, initialization_vector
    )
