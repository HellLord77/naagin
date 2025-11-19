from base64 import b64encode
from collections.abc import AsyncIterable
from collections.abc import Sequence
from hashlib import md5
from secrets import choice

from asyncstdlib import list as alist
from asyncstdlib.itertools import tee as atee
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import CBC
from cryptography.hazmat.primitives.padding import PKCS7
from fastapi import Response
from fastapi.datastructures import Headers
from starlette.routing import Match
from starlette.routing import Router
from starlette.types import Scope

from .cached_resource import CachedResource as CachedResource
from .custom_header import CustomHeader as CustomHeader
from .sqlalchemy_handler import SQLAlchemyHandler as SQLAlchemyHandler


def choices[T: Sequence](population: T, *, k: int = 1) -> list[T]:
    return [choice(population) for _ in range(k)]


def headers_get_split(self: Headers, key: str) -> list[str]:
    value = self.get(key, "")
    return list(filter(None, map(str.strip, value.split(","))))


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


async def response_peek_body(self: Response) -> bytes:
    body_iterator = getattr(self, "body_iterator", None)
    if isinstance(body_iterator, AsyncIterable):
        self.body_iterator, body_iterator = atee(body_iterator)
        return b"".join(await alist(body_iterator))

    return self.body


def encrypt_data(algorithm: AES, data: bytes, initialization_vector: bytes) -> bytes:
    padder = PKCS7(algorithm.block_size).padder()
    encryptor = Cipher(algorithm, CBC(initialization_vector)).encryptor()
    padded_data = padder.update(data) + padder.finalize()
    return encryptor.update(padded_data) + encryptor.finalize()


def encrypt_resource_data(platform_id: int, key: bytes, data: bytes) -> str:
    md5_ = md5(key, usedforsecurity=False)
    encoded_key = md5_.hexdigest().encode()
    md5_.update(str(platform_id).encode())
    initialization_vector = md5_.digest()
    encrypted_data = encrypt_data(AES(encoded_key), data, initialization_vector)
    return b64encode(encrypted_data).decode()
