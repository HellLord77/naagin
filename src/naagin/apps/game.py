from asyncio import Lock
from functools import lru_cache
from http import HTTPStatus
from shutil import rmtree

from fastapi import Request
from fastapi import Response
from fastapi.responses import FileResponse
from fastapi.responses import PlainTextResponse
from fastapi.staticfiles import StaticFiles
from httpx import HTTPStatusError

from naagin import settings
from naagin.exceptions import InternalServerErrorException

logger = settings.logging.logger

app = StaticFiles(directory=settings.data.game_dir)


def not_found_response() -> PlainTextResponse:
    return PlainTextResponse("Not Found\n", HTTPStatus.NOT_FOUND)


@lru_cache
def get_path_lock(_: str) -> Lock:
    return Lock()


async def not_found_handler(request: Request, _: Exception) -> Response:
    if settings.game.offline_mode:
        return not_found_response()

    url_path = request.url.path.removeprefix("/game/")
    path = settings.data.game_dir / url_path
    async with get_path_lock(url_path):
        if not await path.is_file():
            logger.info("Downloading game: %s", url_path)
            try:
                response = await settings.game.client.get(url_path)
                response.raise_for_status()
            except HTTPStatusError as exception:
                if exception.response.status_code == HTTPStatus.NOT_FOUND:
                    return not_found_response()
                else:
                    return InternalServerErrorException.handler(request, exception)
            else:
                if await path.is_dir():
                    rmtree(path)

                await path.parent.mkdir(parents=True, exist_ok=True)
                temp_path = path.with_suffix(".tmp")
                await temp_path.write_bytes(response.content)
                await temp_path.rename(path)
    return FileResponse(path)
