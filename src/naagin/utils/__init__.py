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
from fastapi.responses import StreamingResponse

from naagin.enums import EncodingEnum
from .doaxvv_header import DOAXVVHeader
from .postgresql_handler import PostgreSQLHandler


def get_route_path(scope: MutableMapping[str, Any]) -> str:
    path = scope["path"]
    root_path = scope.get("root_path", "")
    return path.removeprefix(root_path)


def should_endec(scope: MutableMapping[str, Any]) -> bool:
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


async def request_decrypt_body(self: Request, key: bytes, initialization_vector: bytes):
    self._body = decrypt_data(await self.body(), key, initialization_vector)


async def request_decompress_body(self: Request):
    self._body = decompress(await self.body())


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
