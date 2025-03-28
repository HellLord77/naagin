from base64 import b64encode
from hashlib import md5
from http import HTTPStatus
from re import compile

from aiopath import AsyncPath
from filelock import AsyncFileLock
from httpx import HTTPStatusError
from starlette.datastructures import URL
from starlette.responses import FileResponse
from starlette.responses import PlainTextResponse
from starlette.responses import RedirectResponse
from starlette.responses import Response  # noqa: TID251
from starlette.staticfiles import PathLike
from starlette.types import Scope

from naagin import loggers
from naagin import settings
from naagin.classes import StaticFiles
from naagin.exceptions import InternalServerErrorException

etag_pattern = compile(r'^"(?P<md5>[a-f\d]{32}):(?P<mtime>\d+\.\d+)"$')


def not_found_response() -> PlainTextResponse:
    return PlainTextResponse("Not Found\n", HTTPStatus.NOT_FOUND)


async def not_found_handler(path: PathLike, scope: Scope) -> Response:
    full_path = await AsyncPath(settings.data.game_dir / path).resolve()
    try:
        relative_path = full_path.relative_to(settings.data.game_dir)
    except ValueError:
        return not_found_response()

    url = relative_path.as_posix()
    encoded_path = settings.data.temp_dir / b64encode(url.encode()).decode()
    lock_path = encoded_path.with_suffix(".lock")

    async with AsyncFileLock(lock_path):
        if not await full_path.is_file():
            loggers.game.info("GET: %s", url)
            try:
                response = await settings.game.client.get(url)
                response.raise_for_status()
            except HTTPStatusError as exception:
                if exception.response.status_code == HTTPStatus.NOT_FOUND:
                    loggers.game.warning("[bold]Resource[/bold] not found: %s", url)
                    if full_path.name != "index.html":
                        return await not_found_handler(full_path / "index.html", scope)
                    return not_found_response()

                if HTTPStatus(exception.response.status_code).is_redirection:
                    url = URL(exception.response.headers["Location"])
                    return RedirectResponse(f"{scope.get('root_path', '').rstrip('/')}{url.path}")

                raise
            else:
                etag = response.headers.get("ETag", "")
                match = etag_pattern.match(etag)
                if match is None:
                    loggers.game.warning("Unknown [bold]ETag[/bold] string: %s", etag)
                    raise InternalServerErrorException
                md5_ = md5(response.content).hexdigest()  # noqa: S324
                if md5_ != match.group("md5"):
                    loggers.game.warning("[bold]MD5[/bold] mismatch: %s", md5_)
                    raise InternalServerErrorException

                await full_path.parent.mkdir(parents=True, exist_ok=True)
                temp_path = encoded_path.with_suffix(".temp")

                await temp_path.write_bytes(response.content)
                await temp_path.rename(full_path)
    return FileResponse(full_path)


kwargs = {}
if not settings.game.offline_mode:
    kwargs["not_found_handler"] = not_found_handler

app = StaticFiles(directory=settings.data.game_dir, html=True, **kwargs)
