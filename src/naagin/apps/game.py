from asyncio import Lock
from functools import cache
from functools import lru_cache
from shutil import rmtree

from fastapi import HTTPException
from fastapi import Request
from fastapi import status
from fastapi.responses import FileResponse
from fastapi.responses import PlainTextResponse
from fastapi.staticfiles import StaticFiles
from httpx import AsyncClient
from httpx import HTTPStatusError

from naagin import settings

app = StaticFiles(directory=settings.data.game_dir)


@lru_cache
def get_path_lock(_: str):
    return Lock()


@cache
def get_client():
    return AsyncClient(
        base_url=settings.game.base_url, trust_env=not settings.game.no_proxy
    )


async def not_found(request: Request, _: HTTPException):
    if settings.game.offline_mode:
        return PlainTextResponse("Not Found\n", status_code=status.HTTP_404_NOT_FOUND)
    else:
        url_path = request.url.path.removeprefix("/game")
        path = settings.data.game_dir / url_path.removeprefix("/")
        async with get_path_lock(url_path):
            if not await path.is_file():
                client = get_client()
                try:
                    response = await client.get(url_path)
                    response.raise_for_status()
                except HTTPStatusError:
                    return PlainTextResponse(
                        "Not Found\n", status_code=status.HTTP_404_NOT_FOUND
                    )
                else:
                    if await path.is_dir():
                        rmtree(path)

                    await path.parent.mkdir(parents=True, exist_ok=True)
                    temp_path = path.with_suffix(".tmp")
                    await temp_path.write_bytes(response.content)
                    await temp_path.rename(path)
        return FileResponse(path)
