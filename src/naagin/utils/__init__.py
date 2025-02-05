from base64 import b64encode
from secrets import token_bytes
from typing import AsyncGenerator
from typing import AsyncIterable
from zlib import compressobj
from zlib import decompress

from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import CBC
from cryptography.hazmat.primitives.padding import PKCS7
from fastapi import Request
from fastapi.responses import StreamingResponse
from starlette.datastructures import MutableHeaders

from naagin.enums import EncodingEnum
from .doaxvv_header import DOAXVVHeader
from .response_model_exclude_defaults_api_router import (
    ResponseModelExcludeDefaultsAPIRouter,
)
from .sqlalchemy_handler import SQLAlchemyHandler


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


def request_headers(self: Request) -> MutableHeaders:
    headers = self.headers
    if not isinstance(headers, MutableHeaders):
        headers = MutableHeaders(scope=self.scope)
        self._headers = headers
    return headers


async def request_decrypt_body(self: Request, key: bytes, initialization_vector: bytes):
    body = await self.body()
    decrypted = decrypt_data(body, key, initialization_vector)
    self._body = decrypted

    headers = request_headers(self)
    headers["Content-Length"] = str(len(decrypted))


async def request_decompress_body(self: Request):
    body = await self.body()
    decompressed = decompress(body)
    self._body = decompressed

    headers = request_headers(self)
    headers["Content-Length"] = str(len(decompressed))


def response_compress_body(self: StreamingResponse):
    self.body_iterator = iter_compress_data(self.body_iterator)

    del self.headers["Content-Length"]
    self.headers["Content-Type"] = "application/octet-stream"
    DOAXVVHeader.set(self, "Encoding", EncodingEnum.DEFLATE)


def response_encrypt_body(self: StreamingResponse, key: bytes):
    initialization_vector = token_bytes(16)
    self.body_iterator = iter_encrypt_data(
        self.body_iterator, key, initialization_vector
    )

    del self.headers["Content-Length"]
    self.headers["Content-Type"] = "application/octet-stream"
    DOAXVVHeader.set(self, "Encrypted", b64encode(initialization_vector).decode())
