from base64 import b64encode
from hashlib import md5
from http import HTTPMethod
from http import HTTPStatus
from logging import Logger
from mimetypes import guess_type
from re import compile
from typing import override

from anyio import Path as AsyncPath
from filelock import AsyncFileLock
from httpx import AsyncClient
from httpx import HTTPStatusError
from starlette.exceptions import HTTPException  # noqa: TID251
from starlette.responses import FileResponse
from starlette.responses import PlainTextResponse
from starlette.responses import RedirectResponse
from starlette.responses import Response  # noqa: TID251
from starlette.staticfiles import PathLike
from starlette.staticfiles import StaticFiles
from starlette.types import Receive
from starlette.types import Scope
from starlette.types import Send

from naagin import settings

etag_pattern = compile(r"^\"(?P<md5>[a-f\d]{32}):(?P<mtime>\d+(?:\.\d+)?)\"$")


def not_found_response() -> PlainTextResponse:
    return PlainTextResponse("Not Found\n", HTTPStatus.NOT_FOUND)


class CachedResource(StaticFiles):
    directory: AsyncPath

    @override
    def __init__(self, directory: AsyncPath, client: AsyncClient, logger: Logger, offline: bool) -> None:
        super().__init__(directory=directory, html=True)
        self.client = client
        self.logger = logger
        self.offline = offline

    @override
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        try:
            await super().__call__(scope, receive, send)
        except HTTPException as exception:
            if exception.status_code == HTTPStatus.NOT_FOUND:
                if self.offline:
                    response = not_found_response()
                else:
                    path = self.get_path(scope)
                    response = await self.not_found_handler(path, scope)
                await response(scope, receive, send)
            else:
                raise

    async def not_found_handler(self, path: PathLike, scope: Scope) -> Response:
        from naagin.exceptions import InternalServerErrorException  # noqa: PLC0415

        full_path = await (self.directory / path).resolve()
        try:
            relative_path = full_path.relative_to(self.directory)
        except ValueError:
            self.logger.warning("Invalid [bold]resource[/bold] path: %s", scope["path"])
            return not_found_response()

        url = relative_path.as_posix()
        encoded_path = settings.data.temp_dir / b64encode(url.encode()).decode()
        lock_path = encoded_path.with_suffix(".lock")

        async with AsyncFileLock(lock_path):
            if not await full_path.is_file():
                self.logger.info("GET: %s", url)

                async with self.client.stream(HTTPMethod.GET, url) as response:
                    try:
                        response.raise_for_status()
                    except HTTPStatusError:
                        if response.status_code == HTTPStatus.NOT_FOUND:
                            if full_path.name != "index.html":
                                mimetype = guess_type(full_path.name, strict=False)[0]
                                if mimetype is None:
                                    return await self.not_found_handler(full_path / "index.html", scope)
                                self.logger.debug("Guessed [bold]mimetype[/bold]: %s", mimetype)
                            self.logger.warning("[bold]Resource[/bold] not found: %s", url)
                            return not_found_response()

                        if HTTPStatus(response.status_code).is_redirection:
                            location = response.headers["Location"]
                            self.logger.info("[bold]Resource[/bold] redirected: %s", location)
                            return RedirectResponse(location)

                        raise
                    else:
                        etag = response.headers.get("ETag")
                        if etag is None:
                            self.logger.debug("[bold]ETag[/bold] missing")
                            expected_md5 = None
                        else:
                            etag_match = etag_pattern.match(etag)
                            if etag_match is None:
                                self.logger.warning("Invalid [bold]ETag[/bold]: %s", etag)
                                raise InternalServerErrorException
                            expected_md5 = etag_match.group("md5")

                        md5_ = md5(usedforsecurity=False)
                        temp_path = encoded_path.with_suffix(".temp")
                        await temp_path.parent.mkdir(parents=True, exist_ok=True)

                        async with await temp_path.open("wb") as file:
                            async for chunk in response.aiter_bytes():
                                md5_.update(chunk)
                                await file.write(chunk)

                        md5_digest = md5_.hexdigest()
                        if expected_md5 is not None and expected_md5 != md5_digest:
                            self.logger.warning(
                                "[bold]MD5[/bold] mismatch: expected %s, got %s", expected_md5, md5_digest
                            )
                            await temp_path.unlink()
                            raise InternalServerErrorException

                        await full_path.parent.mkdir(parents=True, exist_ok=True)
                        await temp_path.rename(full_path)

        return FileResponse(full_path)
