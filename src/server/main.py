from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Request
from fastapi import status
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import JSONResponse
from uvicorn import run

from . import apps
from . import routers
from . import settings
from .schemas.base import NaaginBaseSchema


@asynccontextmanager
async def lifespan(_: FastAPI):
    async with settings.database.engine.begin() as connection:
        await connection.run_sync(NaaginBaseSchema.metadata.create_all)
    yield
    await settings.database.engine.dispose()


app = FastAPI(title="Naagin", version="0.0.1", lifespan=lifespan)
# noinspection PyTypeChecker
app.add_middleware(GZipMiddleware)

app.include_router(routers.api.router, prefix="/api", tags=["api"])
app.include_router(routers.api01.router, prefix="/api01", tags=["api01"])
app.mount("/game", apps.game.app)


@app.exception_handler(status.HTTP_301_MOVED_PERMANENTLY)
async def moved_permanently(_: Request, __: HTTPException):
    return JSONResponse(
        {"code": status.HTTP_301_MOVED_PERMANENTLY, "message": "cache exception"},
        status.HTTP_301_MOVED_PERMANENTLY,
    )


@app.exception_handler(status.HTTP_401_UNAUTHORIZED)
async def unauthorized(_: Request, __: HTTPException):
    return JSONResponse(
        {"code": 11, "message": "authentication failed"},
        status.HTTP_401_UNAUTHORIZED,
    )


@app.exception_handler(status.HTTP_404_NOT_FOUND)
async def not_found(request: Request, _: HTTPException):
    if request.url.path.startswith("/game"):
        return await apps.game.not_found(request, _)
    else:
        return JSONResponse(
            {"code": status.HTTP_404_NOT_FOUND, "message": "not found"},
            status.HTTP_404_NOT_FOUND,
        )


@app.exception_handler(status.HTTP_405_METHOD_NOT_ALLOWED)
async def method_not_allowed(_: Request, __: HTTPException):
    return JSONResponse(
        {"code": status.HTTP_405_METHOD_NOT_ALLOWED, "message": "method not allowed"},
        status.HTTP_405_METHOD_NOT_ALLOWED,
    )


@app.exception_handler(status.HTTP_500_INTERNAL_SERVER_ERROR)
async def internal_server_error(_: Request, __: HTTPException):
    return JSONResponse(
        {"code": -1, "message": "internal server error"},
        status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


def main():
    run(app)


if __name__ == "__main__":
    main()
