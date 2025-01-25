from zlib import Z_DEFAULT_COMPRESSION

from starlette.datastructures import Headers
from starlette.datastructures import MutableHeaders
from starlette.requests import empty_send
from starlette.types import ASGIApp
from starlette.types import Message
from starlette.types import Receive
from starlette.types import Scope
from starlette.types import Send

from naagin.enums import EncodingEnum
from naagin.utils import DOAXVVHeader
from naagin.utils import should_endec
from naagin.utils.encoder import DeflateEncoder

ENCODING_HEADER = DOAXVVHeader("Encoding")


class DeflateMiddleware:
    def __init__(self, app: ASGIApp, level: int = Z_DEFAULT_COMPRESSION):
        self.app = app
        self.level = level

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        if scope["type"] == "http" and should_endec(scope):
            responder = DeflateResponder(self.app, self.level)
            await responder(scope, receive, send)
        else:
            await self.app(scope, receive, send)


class DeflateResponder:
    def __init__(self, app: ASGIApp, level: int):
        self.app = app
        self.encoder = DeflateEncoder(level)

        self.send = empty_send
        self.initial_message = {}
        self.encoding_set = False
        self.started = False

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        self.send = send
        await self.app(scope, receive, self.send_with_deflate)

    async def send_with_deflate(self, message: Message):
        message_type = message["type"]
        if message_type == "http.response.start":
            self.initial_message = message
            headers = Headers(raw=self.initial_message["headers"])
            self.encoding_set = ENCODING_HEADER in headers
        elif message_type == "http.response.body":
            if self.encoding_set:
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
                        headers = MutableHeaders(raw=self.initial_message["headers"])
                        headers["Content-Type"] = "application/octet-stream"
                        headers[ENCODING_HEADER] = EncodingEnum.DEFLATE

                        body = self.encoder.update(body)
                        if more_body:
                            del headers["Content-Length"]
                        else:
                            body += self.encoder.flush()
                            headers["Content-Length"] = str(len(body))
                    await self.send(self.initial_message)

                message["body"] = body
            await self.send(message)
