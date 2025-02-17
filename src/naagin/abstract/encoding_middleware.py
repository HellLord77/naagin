from abc import ABC
from abc import abstractmethod

from fastapi.datastructures import Headers
from starlette.datastructures import MutableHeaders
from starlette.requests import empty_receive
from starlette.requests import empty_send
from starlette.types import ASGIApp
from starlette.types import Message
from starlette.types import Receive
from starlette.types import Scope
from starlette.types import Send

from naagin.abstract import BaseEncoding
from naagin.utils.encodings import EmptyEncoding


class BaseEncodingMiddleware(ABC):
    receive: Receive
    connection_scope: Scope
    receive_encoding: BaseEncoding

    send: Send
    initial_message: Message
    send_encoding: BaseEncoding

    def __init__(self, app: ASGIApp, *, send_encoded: bool = True) -> None:
        self.app = app
        self.send_encoded = send_encoded

        self.receive = empty_receive
        self.receive_started = False
        self.connection_scope = {}
        self.receive_encoding = EmptyEncoding()

        self.send = empty_send
        self.send_started = False
        self.initial_message = {}
        self.encoding_set = True
        self.send_encoding = EmptyEncoding()

    @abstractmethod
    def is_receive_encoding_set(self, headers: Headers) -> bool:
        raise NotImplementedError

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] == "http":
            self.connection_scope = scope

            headers = Headers(raw=scope["headers"])
            if self.is_receive_encoding_set(headers):
                self.receive = receive
                receive = self.receive_with_decoder

            if self.send_encoded:
                self.send = send
                send = self.send_with_encoder

        await self.app(scope, receive, send)

    @abstractmethod
    async def get_receive_encoding(self, headers: MutableHeaders) -> BaseEncoding:
        raise NotImplementedError

    async def receive_with_decoder(self) -> Message:
        message = await self.receive()
        if message["type"] == "http.request":
            body = message.get("body", b"")
            more_body = message.get("more_body", False)

            if self.receive_started:
                body = self.receive_encoding.update(body)
                if not more_body:
                    body += self.receive_encoding.flush()
            else:
                self.receive_started = True

                if body or more_body:
                    header = MutableHeaders(raw=self.connection_scope["headers"])
                    self.receive_encoding = await self.get_receive_encoding(header)
                    del header["Content-Type"]

                    body = self.receive_encoding.update(body)
                    if more_body:
                        del header["Content-Length"]
                    else:
                        body += self.receive_encoding.flush()
                        header["Content-Length"] = str(len(body))

            message["body"] = body
        return message

    @abstractmethod
    def is_send_encoding_set(self, headers: Headers) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def get_send_encoding(self, headers: MutableHeaders) -> BaseEncoding:
        raise NotImplementedError

    async def send_with_encoder(self, message: Message) -> None:
        message_type = message["type"]
        if message_type == "http.response.start":
            self.initial_message = message
            headers = Headers(raw=message["headers"])
            self.encoding_set = self.is_send_encoding_set(headers)
        elif message_type == "http.response.body":
            if self.encoding_set:
                if not self.send_started:
                    self.send_started = True
                    await self.send(self.initial_message)
            else:
                body = message.get("body", b"")
                more_body = message.get("more_body", False)

                if self.send_started:
                    body = self.send_encoding.update(body)
                    if not more_body:
                        body += self.send_encoding.flush()
                else:
                    self.send_started = True

                    if body or more_body:
                        headers = MutableHeaders(raw=self.initial_message["headers"])
                        self.send_encoding = await self.get_send_encoding(headers)
                        headers["Content-Type"] = "application/octet-stream"

                        body = self.send_encoding.update(body)
                        if more_body:
                            del headers["Content-Length"]
                        else:
                            body += self.send_encoding.flush()
                            headers["Content-Length"] = str(len(body))
                    await self.send(self.initial_message)

                message["body"] = body
            await self.send(message)
