from collections.abc import Awaitable
from collections.abc import Callable
from datetime import UTC
from datetime import datetime
from http import HTTPStatus
from operator import itemgetter
from pathlib import Path  # noqa: TID251
from stat import S_ISDIR
from typing import override

from aiopath import AsyncPath
from starlette.datastructures import URL
from starlette.exceptions import HTTPException  # noqa: TID251
from starlette.requests import Request  # noqa: TID251
from starlette.responses import PlainTextResponse
from starlette.responses import RedirectResponse
from starlette.responses import Response  # noqa: TID251
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from starlette.types import Receive
from starlette.types import Scope
from starlette.types import Send

from naagin.enums import AutoIndexFormatEnum
from naagin.models.auto_index import AutoIndexModel
from naagin.models.auto_index import AutoIndexXMLModel
from naagin.utils.responses import LXMLResponse

TemplateResponse = Jinja2Templates(Path(__file__).parent / "templates").TemplateResponse


class CustomStaticFiles(StaticFiles):
    @override
    def __init__(
        self,
        *args,  # noqa: ANN002
        autoindex: bool = False,
        autoindex_format: AutoIndexFormatEnum = AutoIndexFormatEnum.HTML,
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
            child_path: AsyncPath
            dir_ = {}
            stat = await child_path.stat()
            dir_["name"] = child_path.name
            dir_["mtime"] = datetime.fromtimestamp(stat.st_mtime, UTC)
            if S_ISDIR(stat.st_mode):
                dirs.append(dir_)
            else:
                dir_["size"] = stat.st_size
                files.append(dir_)

        sorted(dirs, key=itemgetter("name"))
        sorted(files, key=itemgetter("name"))

        match self.autoindex_format:
            case AutoIndexFormatEnum.HTML:
                base = path.relative_to(self.directory).as_posix()
                if base == ".":
                    base = ""

                return TemplateResponse(
                    Request(scope), "auto_index.html.jinja", {"base": base, "dirs": dirs, "files": files}
                )
            case AutoIndexFormatEnum.XML:
                return LXMLResponse(AutoIndexXMLModel(root=dirs + files).to_xml_tree())
            case AutoIndexFormatEnum.JSON:
                return Response(AutoIndexModel(root=dirs + files).model_dump_json(), media_type="application/json")
            case _:
                raise NotImplementedError
