import os

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Request
from fastapi import status
from fastapi.responses import FileResponse
from fastapi.responses import PlainTextResponse
from fastapi.staticfiles import StaticFiles
from httpx import AsyncClient

from .. import config

app = FastAPI()

app.mount("/game", StaticFiles(directory=os.path.join(config.DATA_DIR, "game")))


@app.exception_handler(status.HTTP_404_NOT_FOUND)
async def not_found(request: Request, _: HTTPException):
    path = request.url.path.removeprefix("/game")
    async with AsyncClient() as client:
        response = await client.get(f"https://game.doaxvv.com{path}")
        if response.status_code == status.HTTP_200_OK:
            path_ = os.path.join(config.DATA_DIR, "game", path.removeprefix("/"))
            os.makedirs(os.path.dirname(path_), exist_ok=True)
            with open(path_, "wb") as file:
                file.write(response.content)
            return FileResponse(path_)
        else:
            return PlainTextResponse("Not found\n", status.HTTP_404_NOT_FOUND)
