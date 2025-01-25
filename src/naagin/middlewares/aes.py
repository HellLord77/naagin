from base64 import b64encode
from secrets import token_bytes

from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import CBC
from cryptography.hazmat.primitives.padding import PKCS7
from fastapi import Request
from starlette.datastructures import Headers
from starlette.datastructures import MutableHeaders
from starlette.requests import empty_send
from starlette.types import ASGIApp
from starlette.types import Message
from starlette.types import Receive
from starlette.types import Scope
from starlette.types import Send

from naagin.utils import DOAXVVHeader
from naagin.utils import should_endec
from naagin.utils.encoder import CipherEncoder
from naagin.utils.encoder import MultiEncoder
from naagin.utils.encoder import PaddingEncoder

ENCRYPTED_HEADER = DOAXVVHeader("Encrypted")


class AESMiddleware:
    def __init__(self, app: ASGIApp):
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        if scope["type"] == "http" and should_endec(scope):
            responder = AESResponder(self.app)
            await responder(scope, receive, send)
        else:
            await self.app(scope, receive, send)


class AESResponder:
    request: Request
    encoder: MultiEncoder

    def __init__(self, app: ASGIApp):
        self.app = app
        self.initialization_vector = token_bytes(16)

        self.send = empty_send
        self.initial_message = {}
        self.encrypted_set = False
        self.started = False

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        self.request = Request(scope)
        self.send = send
        await self.app(scope, receive, self.send_with_aes)

    async def send_with_aes(self, message: Message):
        message_type = message["type"]
        if message_type == "http.response.start":
            self.initial_message = message
            headers = Headers(raw=self.initial_message["headers"])
            self.encrypted_set = ENCRYPTED_HEADER in headers
        elif message_type == "http.response.body":
            if self.encrypted_set:
                if not self.started:
                    self.started = True
                    await self.send(self.initial_message)
            else:
                body = message.get("body", b"")
                more_body = message.get("more_body", False)

                if self.started:
                    body = self.encoder.update(body)
                    if not more_body:
                        body += self.encoder.flush()
                else:
                    self.started = True

                    if body or more_body:
                        self.encoder = MultiEncoder(
                            PaddingEncoder(PKCS7(AES.block_size).padder()),
                            CipherEncoder(
                                Cipher(
                                    AES(self.request.state.session_key),
                                    CBC(self.initialization_vector),
                                ).encryptor()
                            ),
                        )

                        headers = MutableHeaders(raw=self.initial_message["headers"])
                        headers["Content-Type"] = "application/octet-stream"
                        headers[ENCRYPTED_HEADER] = b64encode(
                            self.initialization_vector
                        ).decode()

                        body = self.encoder.update(body)
                        if more_body:
                            del headers["Content-Length"]
                        else:
                            body += self.encoder.flush()
                            headers["Content-Length"] = str(len(body))
                    await self.send(self.initial_message)

                message["body"] = body
            await self.send(message)
