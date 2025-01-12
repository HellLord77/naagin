import functools
import shutil
from asyncio import Lock

from fastapi import HTTPException
from fastapi import Request
from fastapi import status
from fastapi.responses import FileResponse
from fastapi.responses import PlainTextResponse
from fastapi.staticfiles import StaticFiles
from httpx import AsyncClient
from httpx import HTTPStatusError

from .. import config
from .. import consts

app = StaticFiles(directory=consts.GAME_DIR)


@functools.lru_cache
def get_path_lock(_: str):
    return Lock()


@functools.cache
def get_client():
    return AsyncClient(base_url=consts.GAME_URL, trust_env=not config.NO_PROXY)


async def not_found(request: Request, _: HTTPException):
    url_path = request.url.path.removeprefix("/game")
    path = consts.GAME_DIR / url_path.removeprefix("/")
    async with get_path_lock(url_path):
        if not await path.is_file():
            client = get_client()
            try:
                response = await client.get(url_path)
                response.raise_for_status()
            except HTTPStatusError:
                return PlainTextResponse(
                    "Not Found", status_code=status.HTTP_404_NOT_FOUND
                )
            else:
                if await path.is_dir():
                    shutil.rmtree(path)

                await path.parent.mkdir(parents=True, exist_ok=True)
                temp_path = path.with_suffix(".tmp")
                await temp_path.write_bytes(response.content)
                temp_path.rename(path)
    return FileResponse(path)
