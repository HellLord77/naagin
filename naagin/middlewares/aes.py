from base64 import b64decode
from base64 import b64encode
from secrets import token_bytes
from typing import override

from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers import CipherContext
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import CBC
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.primitives.padding import PaddingContext
from starlette.datastructures import Headers
from starlette.datastructures import MutableHeaders
from starlette.requests import Request
from starlette.types import ASGIApp

from naagin.abstract import BaseEncodingMiddleware
from naagin.classes import AsyncSession
from naagin.enums import DOAXVVHeaderEnum
from naagin.exceptions import AuthenticationFailedException
from naagin.providers import provide_session
from naagin.utils import DOAXVVHeader


class AESMiddleware(BaseEncodingMiddleware):
    decryptor: CipherContext
    unpadder: PaddingContext
    padder: PaddingContext
    encryptor: CipherContext

    header = DOAXVVHeaderEnum.ENCRYPTED

    @override
    def __init__(self, app: ASGIApp, *, send_encoded: bool = True, database: AsyncSession) -> None:
        super().__init__(app, send_encoded=send_encoded)
        self.database = database

    def should_receive_with_decoder(self, headers: Headers) -> bool:
        return self.header in headers

    async def init_decoder(self, headers: MutableHeaders) -> None:
        request = Request(self.connection_scope)
        session = await provide_session(request, database=self.database)
        initialization_vector = b64decode(request.headers[self.header])

        del headers[self.header]
        self.decryptor = Cipher(AES(session.key), CBC(initialization_vector)).decryptor()
        self.unpadder = PKCS7(AES.block_size).unpadder()

    def update_decoder(self, data: bytes) -> bytes:
        return self.unpadder.update(self.decryptor.update(data))

    def flush_decoder(self) -> bytes:
        return self.unpadder.update(self.decryptor.finalize()) + self.unpadder.finalize()

    def should_send_with_encoder(self, headers: Headers) -> bool:
        return self.header not in headers

    async def init_encoder(self, headers: MutableHeaders) -> bool:
        request = Request(self.connection_scope)
        try:
            session = await provide_session(request, database=self.database)
        except AuthenticationFailedException:
            return False
        initialization_vector = token_bytes(16)

        headers[DOAXVVHeader(self.header)] = b64encode(initialization_vector).decode()
        self.padder = PKCS7(AES.block_size).padder()
        self.encryptor = Cipher(AES(session.key), CBC(initialization_vector)).encryptor()
        return True

    def update_encoder(self, data: bytes) -> bytes:
        return self.encryptor.update(self.padder.update(data))

    def flush_encoder(self) -> bytes:
        return self.encryptor.update(self.padder.finalize()) + self.encryptor.finalize()
