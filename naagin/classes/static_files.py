from http import HTTPStatus
from typing import override

from starlette.exceptions import HTTPException  # noqa: TID251
from starlette.responses import PlainTextResponse
from starlette.types import Receive
from starlette.types import Scope
from starlette.types import Send
from static_files_asgi import StaticFiles


class CustomStaticFiles(StaticFiles):
    @override
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        try:
            await super().__call__(scope, receive, send)
        except HTTPException as exception:
            if exception.status_code == HTTPStatus.NOT_FOUND:
                response = PlainTextResponse("Not Found\n", HTTPStatus.NOT_FOUND)
                await response(scope, receive, send)
            raise
