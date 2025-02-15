from base64 import b64encode
from collections.abc import AsyncGenerator
from collections.abc import AsyncIterable
from collections.abc import Sequence
from json import JSONDecodeError
from secrets import choice
from secrets import token_bytes
from zlib import compressobj
from zlib import decompress

from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import CBC
from cryptography.hazmat.primitives.padding import PKCS7
from fastapi import Request
from starlette.datastructures import MutableHeaders
from starlette.middleware.base import _StreamingResponse
from starlette.routing import Match
from starlette.routing import Router
from starlette.types import Scope

from naagin.decorators import async_request_cache
from naagin.enums import EncodingEnum

from .doaxvv_header import DOAXVVHeader as DOAXVVHeader
from .sqlalchemy_handler import SQLAlchemyHandler as SQLAlchemyHandler


def choices[T: Sequence](population: T, *, k: int = 1) -> list[T]:
    return [choice(population) for _ in range(k)]


def decrypt_data(data: bytes, key: bytes, initialization_vector: bytes) -> bytes:
    algorithm = AES(key)
    mode = CBC(initialization_vector)
    decryptor = Cipher(algorithm, mode).decryptor()
    unpadder = PKCS7(AES.block_size).unpadder()

    return unpadder.update(decryptor.update(data) + decryptor.finalize()) + unpadder.finalize()


async def iter_compress_data(data_stream: AsyncIterable[bytes]) -> AsyncGenerator[bytes]:
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


@async_request_cache
async def match_request(request: Request, router: Router, match: Match = Match.FULL) -> bool:
    matches = router_matches(router, request.scope)
    return matches[0].value >= match.value


def router_matches(self: Router, scope: Scope) -> tuple[Match, Scope]:
    partial_matches: tuple[Match, Scope] = Match.NONE, {}
    for route in self.routes:
        matches = route.matches(scope)
        match matches[0]:
            case Match.FULL:
                return matches
            case Match.PARTIAL if partial_matches[0] == Match.NONE:
                partial_matches = matches
    return partial_matches


def request_headers(self: Request) -> MutableHeaders:
    headers = self.headers
    if not isinstance(headers, MutableHeaders):
        headers = MutableHeaders(scope=self.scope)
        self._headers = headers
    return headers


async def request_headers_try_set_item_content_type_application_json(self: Request) -> None:
    content_type = self.headers.get("Content-Type")
    if content_type == "application/octet-stream":
        try:
            await self.json()
        except (UnicodeDecodeError, JSONDecodeError):
            pass
        else:
            headers = request_headers(self)
            headers["Content-Type"] = "application/json"


async def request_decompress_body(self: Request) -> None:
    body = await self.body()
    decompressed = decompress(body)
    self._body = decompressed

    headers = request_headers(self)
    headers["Content-Length"] = str(len(decompressed))
    await request_headers_try_set_item_content_type_application_json(self)


async def request_decrypt_body(self: Request, key: bytes, initialization_vector: bytes) -> None:
    body = await self.body()
    decrypted = decrypt_data(body, key, initialization_vector)
    self._body = decrypted

    headers = request_headers(self)
    headers["Content-Length"] = str(len(decrypted))
    await request_headers_try_set_item_content_type_application_json(self)


def response_compress_body(self: _StreamingResponse) -> None:
    self.body_iterator = iter_compress_data(self.body_iterator)

    del self.headers["Content-Length"]
    self.headers["Content-Type"] = "application/octet-stream"
    DOAXVVHeader.set(self, "Encoding", EncodingEnum.DEFLATE)


def response_encrypt_body(self: _StreamingResponse, key: bytes) -> None:
    initialization_vector = token_bytes(16)
    self.body_iterator = iter_encrypt_data(self.body_iterator, key, initialization_vector)

    del self.headers["Content-Length"]
    self.headers["Content-Type"] = "application/octet-stream"
    DOAXVVHeader.set(self, "Encrypted", b64encode(initialization_vector).decode())
