from collections.abc import Awaitable
from collections.abc import Callable
from http import HTTPStatus
from typing import override

from aiopath import AsyncPath
from starlette.exceptions import HTTPException  # noqa: TID251
from starlette.responses import PlainTextResponse
from starlette.responses import Response  # noqa: TID251
from starlette.types import Receive
from starlette.types import Scope
from starlette.types import Send
from static_files_asgi import StaticFiles


class CustomStaticFiles(StaticFiles):
    directory: AsyncPath

    @override
    def __init__(
        self,
        *args,  # noqa: ANN002
        not_found_handler: Callable[[AsyncPath], Awaitable[Response]],
        **kwargs,  # noqa: ANN003
    ) -> None:
        super().__init__(*args, **kwargs)
        self.not_found_handler = not_found_handler

    @override
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        try:
            await super().__call__(scope, receive, send)
        except HTTPException as exception:
            if exception.status_code == HTTPStatus.NOT_FOUND:
                response = PlainTextResponse("Not Found\n", HTTPStatus.NOT_FOUND)
                await response(scope, receive, send)
            raise

    @override
    async def get_response(self, path: str, scope: Scope) -> Response:
        try:
            return await super().get_response(path, scope)
        except HTTPException as exception:
            if exception.status_code == HTTPStatus.NOT_FOUND:
                return await self.not_found_handler(self.directory / path)
            raise
