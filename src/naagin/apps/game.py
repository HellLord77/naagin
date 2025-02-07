from asyncio import Lock
from functools import cache
from functools import lru_cache
from http import HTTPStatus
from shutil import rmtree

from fastapi import HTTPException
from fastapi import Request
from fastapi import Response
from fastapi.responses import FileResponse
from fastapi.responses import PlainTextResponse
from fastapi.staticfiles import StaticFiles
from httpx import AsyncClient
from httpx import HTTPStatusError

from naagin import settings

app = StaticFiles(directory=settings.data.game_dir)


def not_found_response() -> PlainTextResponse:
    return PlainTextResponse("Not Found\n", HTTPStatus.NOT_FOUND)


@lru_cache
def get_path_lock(_: str) -> Lock:
    return Lock()


@cache
def get_client() -> AsyncClient:
    return AsyncClient(base_url=settings.game.base_url, trust_env=not settings.game.no_proxy)


async def not_found_handler(request: Request, _: HTTPException) -> Response:
    if settings.game.offline_mode:
        return not_found_response()
    else:
        url_path = request.url.path.removeprefix("/game/")
        path = settings.data.game_dir / url_path
        async with get_path_lock(url_path):
            if not await path.is_file():
                client = get_client()
                try:
                    response = await client.get(url_path)
                    response.raise_for_status()
                except HTTPStatusError:
                    return not_found_response()
                else:
                    if await path.is_dir():
                        rmtree(path)

                    await path.parent.mkdir(parents=True, exist_ok=True)
                    temp_path = path.with_suffix(".tmp")
                    await temp_path.write_bytes(response.content)
                    await temp_path.rename(path)
        return FileResponse(path)
