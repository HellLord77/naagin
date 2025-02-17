from base64 import b64decode
from base64 import b64encode
from secrets import token_bytes
from typing import override

from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import CBC
from cryptography.hazmat.primitives.padding import PKCS7
from fastapi import Request
from fastapi.datastructures import Headers
from starlette.datastructures import MutableHeaders
from starlette.types import ASGIApp

from naagin.abstract import BaseEncoding
from naagin.abstract import BaseEncodingMiddleware
from naagin.classes import AsyncSession
from naagin.providers import provide_session_
from naagin.utils import DOAXVVHeader
from naagin.utils.encodings import MultiEncoding
from naagin.utils.encodings import UpdateFinalizeEncoding


class AESMiddleware(BaseEncodingMiddleware):
    send_header = DOAXVVHeader("Encrypted")
    receive_header = str(send_header)

    @override
    def __init__(self, app: ASGIApp, *, send_encoded: bool = True, session: AsyncSession) -> None:
        super().__init__(app, send_encoded=send_encoded)
        self.session = session

    def is_receive_encoding_set(self, headers: Headers) -> bool:
        return self.receive_header in headers

    async def get_receive_encoding(self, headers: MutableHeaders) -> BaseEncoding:
        request = Request(scope=self.connection_scope)
        session = await provide_session_(request, session=self.session)
        initialization_vector = b64decode(request.headers[self.receive_header])

        del headers[self.receive_header]
        return MultiEncoding(
            UpdateFinalizeEncoding(Cipher(AES(session.session_key), CBC(initialization_vector)).decryptor()),
            UpdateFinalizeEncoding(PKCS7(AES.block_size).unpadder()),
        )

    def is_send_encoding_set(self, headers: Headers) -> bool:
        return self.send_header in headers

    async def get_send_encoding(self, headers: MutableHeaders) -> BaseEncoding:
        request = Request(scope=self.connection_scope)
        session = await provide_session_(request, session=self.session)
        initialization_vector = token_bytes(16)

        headers[self.send_header] = b64encode(initialization_vector).decode()
        return MultiEncoding(
            UpdateFinalizeEncoding(PKCS7(AES.block_size).padder()),
            UpdateFinalizeEncoding(Cipher(AES(session.session_key), CBC(initialization_vector)).encryptor()),
        )
