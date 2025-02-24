from collections.abc import Awaitable
from collections.abc import Callable
from datetime import UTC
from datetime import datetime
from http import HTTPStatus
from stat import S_ISDIR
from typing import override

from aiopath import AsyncPath
from starlette.datastructures import URL
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import PlainTextResponse
from starlette.responses import RedirectResponse
from starlette.responses import Response
from starlette.staticfiles import StaticFiles
from starlette.types import Receive
from starlette.types import Scope
from starlette.types import Send

from .enums import FormatEnum
from .models import DirectoryModel
from .models import FileModel
from .models import ListModel
from .responses import PydanticJSONResponse
from .responses import PydanticXMLResponse
from .responses import TemplateResponse


class CustomStaticFiles(StaticFiles):
    @override
    def __init__(
        self,
        *args,  # noqa: ANN002
        autoindex: bool = False,
        autoindex_format: FormatEnum = FormatEnum.HTML,
        not_found_handler: Callable[[AsyncPath], Awaitable[Response]] | None = None,
        **kwargs,  # noqa: ANN003
    ) -> None:
        super().__init__(*args, **kwargs)

        self.autoindex = autoindex
        self.autoindex_format = autoindex_format
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
                full_path = await AsyncPath(self.directory, path).resolve()

                if full_path.is_relative_to(self.directory):
                    if self.autoindex and await full_path.is_dir():
                        if not scope["path"].endswith("/"):
                            url = URL(scope=scope)
                            return RedirectResponse(url.replace(path=url.path + "/"))
                        return await self.autoindex_response(full_path, scope)

                    if self.not_found_handler is not None:
                        return await self.not_found_handler(full_path)
            raise

    async def autoindex_response(self, path: AsyncPath, scope: Scope) -> Response:
        dirs = []
        files = []
        async for child_path in path.iterdir():
            stat = await child_path.stat()
            mtime = datetime.fromtimestamp(stat.st_mtime, UTC)
            if S_ISDIR(stat.st_mode):
                dir_ = DirectoryModel(name=child_path.name, mtime=mtime)
                dirs.append(dir_)
            else:
                file = FileModel(name=child_path.name, size=stat.st_size, mtime=mtime)
                files.append(file)

        if self.autoindex_format == FormatEnum.HTML:
            root = path.relative_to(self.directory).as_posix()
            if root == ".":
                root = ""
            return TemplateResponse(
                Request(scope), "autoindex.html.jinja", {"root": root, "dirs": dirs, "files": files}
            )

        list_ = ListModel(root=dirs + files)
        match self.autoindex_format:
            case FormatEnum.XML:
                return PydanticXMLResponse(list_)
            case FormatEnum.JSON:
                return PydanticJSONResponse(list_)
            case _:
                raise NotImplementedError
