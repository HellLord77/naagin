from http import HTTPStatus

from fastapi import Request
from fastapi import Response
from fastapi.responses import FileResponse
from fastapi.responses import PlainTextResponse
from fastapi.staticfiles import StaticFiles
from filelock import AsyncFileLock
from httpx import HTTPStatusError

from naagin import loggers
from naagin import settings
from naagin.exceptions import InternalServerErrorException

app = StaticFiles(directory=settings.data.game_dir)


def not_found_response() -> PlainTextResponse:
    return PlainTextResponse("Not Found\n", HTTPStatus.NOT_FOUND)


async def get_lock(relative_path: str) -> AsyncFileLock:
    lock_path = settings.data.temp_dir / "lock" / relative_path
    await lock_path.parent.mkdir(parents=True, exist_ok=True)
    return AsyncFileLock(lock_path, is_singleton=True)


async def not_found_handler(request: Request, _: Exception) -> Response:
    if settings.game.offline_mode:
        return not_found_response()

    url_path = request.url.path.removeprefix("/game/")
    path = settings.data.game_dir / url_path
    async with await get_lock(url_path):
        if not await path.is_file():
            loggers.game.info("Downloading: %s", url_path)
            try:
                response = await settings.game.client.get(url_path)
                response.raise_for_status()
            except HTTPStatusError as exception:
                if exception.response.status_code == HTTPStatus.NOT_FOUND:
                    return not_found_response()

                return InternalServerErrorException.handler(request, exception)
            else:
                if await path.is_dir():
                    raise InternalServerErrorException

                await path.parent.mkdir(parents=True, exist_ok=True)
                temp_path = path.with_suffix(".temp")
                await temp_path.write_bytes(response.content)
                await temp_path.rename(path)
    return FileResponse(path)
