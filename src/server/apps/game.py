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
from httpx import URL

from .. import config

app = FastAPI()

app.mount("/game", StaticFiles(directory=config.DATA_DIR / "game"))

not_found_lock = functools.lru_cache(lambda _: Lock())


@app.exception_handler(status.HTTP_404_NOT_FOUND)
async def not_found(request: Request, _: HTTPException):
    url_path = request.url.path.removeprefix("/game")
    path = config.DATA_DIR / "game" / url_path.removeprefix("/")
    async with not_found_lock(url_path):
        if not path.is_file():
            async with AsyncClient() as client:
                url = URL(url_path).copy_with(scheme="https", host="game.doaxvv.com")
                try:
                    response = await client.get(url)
                    response.raise_for_status()
                except HTTPStatusError:
                    return PlainTextResponse("Not found\n", status.HTTP_404_NOT_FOUND)

                path.parent.mkdir(parents=True, exist_ok=True)
                temp_path = path.with_suffix(".tmp")
                temp_path.write_bytes(response.content)
                temp_path.rename(path)
        return FileResponse(path)
