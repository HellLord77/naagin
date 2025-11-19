from abc import ABC
from abc import abstractmethod
from http import HTTPStatus

from starlette.datastructures import Headers  # noqa: TID251
from starlette.datastructures import MutableHeaders
from starlette.requests import empty_receive
from starlette.requests import empty_send
from starlette.types import ASGIApp
from starlette.types import Message
from starlette.types import Receive
from starlette.types import Scope
from starlette.types import Send


class BaseEncodingMiddleware(ABC):
    receive: Receive
    connection_scope: Scope

    send: Send
    start_message: Message

    def __init__(self, app: ASGIApp, *, send_encoded: bool = True) -> None:
        self.app = app
        self.send_encoded = send_encoded

        self.receive = empty_receive
        self.receive_started = False
        self.connection_scope = {}

        self.send = empty_send
        self.send_started = False
        self.start_message = {}
        self.should_encode = False

    @abstractmethod
    def should_receive_with_decoder(self, headers: Headers) -> bool:
        raise NotImplementedError

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] == "http":
            self.connection_scope = scope

            headers = Headers(raw=scope["headers"])
            if self.should_receive_with_decoder(headers):
                self.receive = receive
                receive = self.receive_with_decoder

            if self.send_encoded:
                self.send = send
                send = self.send_with_encoder

        await self.app(scope, receive, send)

    @abstractmethod
    async def init_decoder(self, headers: MutableHeaders) -> None:
        raise NotImplementedError

    @abstractmethod
    def update_decoder(self, data: bytes) -> bytes:
        raise NotImplementedError

    @abstractmethod
    def flush_decoder(self) -> bytes:
        raise NotImplementedError

    async def receive_with_decoder(self) -> Message:
        message = await self.receive()
        if message["type"] == "http.request":
            body = message.get("body", b"")
            more_body = message.get("more_body", False)

            if self.receive_started:
                body = self.update_decoder(body)
                if not more_body:
                    body += self.flush_decoder()
            else:
                self.receive_started = True

                if body or more_body:
                    headers = MutableHeaders(raw=self.connection_scope["headers"])
                    await self.init_decoder(headers)
                    del headers["Content-Type"]

                    body = self.update_decoder(body)
                    if more_body:
                        del headers["Content-Length"]
                    else:
                        body += self.flush_decoder()
                        headers["Content-Length"] = str(len(body))

            message["body"] = body
        return message

    @abstractmethod
    def should_send_with_encoder(self, headers: Headers) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def init_encoder(self, headers: MutableHeaders) -> bool:
        raise NotImplementedError

    @abstractmethod
    def update_encoder(self, data: bytes) -> bytes:
        raise NotImplementedError

    @abstractmethod
    def flush_encoder(self) -> bytes:
        raise NotImplementedError

    async def send_with_encoder(self, message: Message) -> None:
        message_type = message["type"]
        if message_type == "http.response.start":
            self.start_message = message
            self.should_encode = HTTPStatus(message["status"]).is_success and self.should_send_with_encoder(
                Headers(raw=message["headers"])
            )
        elif message_type == "http.response.body":
            if self.should_encode:
                body = message.get("body", b"")
                more_body = message.get("more_body", False)

                if self.send_started:
                    body = self.update_encoder(body)
                    if not more_body:
                        body += self.flush_encoder()
                else:
                    self.send_started = True

                    if body or more_body:
                        headers = MutableHeaders(raw=self.start_message["headers"])
                        if await self.init_encoder(headers):
                            headers["Content-Type"] = "application/octet-stream"

                            body = self.update_encoder(body)
                            if more_body:
                                del headers["Content-Length"]
                            else:
                                body += self.flush_encoder()
                                headers["Content-Length"] = str(len(body))
                        else:
                            self.should_encode = False
                    await self.send(self.start_message)

                message["body"] = body
            elif not self.send_started:
                self.send_started = True
                await self.send(self.start_message)
            await self.send(message)
