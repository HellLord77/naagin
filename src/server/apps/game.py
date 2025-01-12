import functools
from asyncio import Lock

from fastapi import FastAPI
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

app = FastAPI()

app.mount("/game", StaticFiles(directory=consts.GAME_DIR))

get_async_client = functools.cache(
    lambda: AsyncClient(base_url=consts.GAME_URL, trust_env=not config.NO_PROXY)
)
get_path_lock = functools.lru_cache(lambda _: Lock())


@app.exception_handler(status.HTTP_404_NOT_FOUND)
async def not_found(request: Request, _: HTTPException):
    url_path = request.url.path.removeprefix("/game")
    path = consts.GAME_DIR / url_path.removeprefix("/")
    async with get_path_lock(url_path):
        if not path.is_file():
            try:
                response = await get_async_client().get(url_path)
                response.raise_for_status()
            except HTTPStatusError:
                return PlainTextResponse(
                    "Not Found", status_code=status.HTTP_404_NOT_FOUND
                )
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                temp_path = path.with_suffix(".tmp")
                temp_path.write_bytes(response.content)
                temp_path.rename(path)
    return FileResponse(path)
