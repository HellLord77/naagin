from shutil import COPY_BUFSIZE

from starlette.requests import empty_receive
from starlette.types import ASGIApp
from starlette.types import Message
from starlette.types import Receive
from starlette.types import Scope
from starlette.types import Send

from naagin.exceptions import InternalServerErrorException


class LimitingBodyRequestMiddleware:
    receive: Receive

    def __init__(self, app: ASGIApp, *, maximum_size: int = COPY_BUFSIZE) -> None:
        self.app = app
        self.maximum_size = maximum_size

        self.receive = empty_receive
        self.received_size = 0

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] == "http":
            self.receive = receive
            receive = self.receive_with_limiting

        await self.app(scope, receive, send)

    async def receive_with_limiting(self) -> Message:
        message = await self.receive()
        if message["type"] == "http.request":
            body = message.get("body", b"")

            self.received_size += len(body)
            if self.received_size > self.maximum_size:
                raise InternalServerErrorException

        return message
