from collections.abc import AsyncGenerator
from collections.abc import Callable
from functools import partial
from typing import override

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.base import RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import ASGIApp

from naagin.exceptions import InternalServerErrorException


class LimitBodyRequestMiddleware(BaseHTTPMiddleware):
    @override
    def __init__(self, app: ASGIApp, *, maximum_size: int) -> None:
        super().__init__(app)
        self.maximum_size = maximum_size

    @override
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        request.stream = partial(self.stream, request.stream)
        return await call_next(request)

    async def stream(self, stream: Callable[[], AsyncGenerator[bytes]]) -> AsyncGenerator[bytes]:
        stream_size = 0
        async for chunk in stream():  # TODO: requires iter decompress, decrypt
            stream_size += len(chunk)
            if stream_size > self.maximum_size:
                raise InternalServerErrorException
            yield chunk
