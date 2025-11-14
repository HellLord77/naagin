from collections.abc import Awaitable
from collections.abc import Callable
from http import HTTPStatus
from typing import override

from starlette.exceptions import HTTPException  # noqa: TID251
from starlette.responses import Response  # noqa: TID251
from starlette.staticfiles import PathLike
from starlette.staticfiles import StaticFiles
from starlette.types import Receive
from starlette.types import Scope
from starlette.types import Send


class CustomStaticFiles(StaticFiles):
    @override
    def __new__(
        cls,
        *args,  # noqa: ANN002
        not_found_handler: Callable[[PathLike, Scope], Awaitable[Response]] | None = None,
        **kwargs,  # noqa: ANN003
    ) -> StaticFiles:
        return StaticFiles(*args, **kwargs) if not_found_handler is None else super().__new__(cls)

    @override
    def __init__(
        self,
        *args,  # noqa: ANN002
        not_found_handler: Callable[[PathLike, Scope], Awaitable[Response]],
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
                path = self.get_path(scope)
                response = await self.not_found_handler(path, scope)
                await response(scope, receive, send)
            else:
                raise
