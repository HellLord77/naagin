from contextlib import asynccontextmanager
from http import HTTPStatus

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Request
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import JSONResponse
from uvicorn import run

from . import apps
from . import routers
from . import settings
from .exceptions import InternalServerErrorException
from .exceptions import InvalidParameterException
from .exceptions import MethodNotAllowedException
from .exceptions import NotFoundException
from .exceptions.base import BaseException
from .models.utils import ExceptionModel
from .schemas.base import BaseSchema


@asynccontextmanager
async def lifespan(_: FastAPI):
    async with settings.database.engine.begin() as connection:
        # await connection.run_sync(BaseSchema.metadata.drop_all)
        await connection.run_sync(BaseSchema.metadata.create_all)
    yield
    await settings.database.engine.dispose()


app = FastAPI(title="Naagin", version="0.0.1", lifespan=lifespan)
app.add_middleware(GZipMiddleware)

app.include_router(routers.api.router, prefix="/api", tags=["api"])
app.include_router(routers.api01.router, prefix="/api01", tags=["api01"])
app.mount("/game", apps.game.app)


@app.exception_handler(HTTPStatus.MOVED_PERMANENTLY)
async def moved_permanently_handler(_: Request, __: HTTPException):
    return JSONResponse(
        {"code": HTTPStatus.MOVED_PERMANENTLY, "message": "cache exception"},
        HTTPStatus.MOVED_PERMANENTLY,
    )


@app.exception_handler(HTTPStatus.NOT_FOUND)
async def not_found_handler(request: Request, _: HTTPException):
    if request.url.path.startswith("/game"):
        return await apps.game.not_found_handler(request, _)
    else:
        return await base_exception_handler(request, NotFoundException())


@app.exception_handler(HTTPStatus.METHOD_NOT_ALLOWED)
async def method_not_allowed_handler(request: Request, _: HTTPException):
    return await base_exception_handler(request, MethodNotAllowedException())


@app.exception_handler(HTTPStatus.UNPROCESSABLE_CONTENT)
async def unprocessable_content_handler(request: Request, _: HTTPException):
    return await base_exception_handler(request, InvalidParameterException())


@app.exception_handler(HTTPStatus.INTERNAL_SERVER_ERROR)
async def internal_server_error_handler(request: Request, _: HTTPException):
    return await base_exception_handler(request, InternalServerErrorException())


@app.exception_handler(BaseException)
async def base_exception_handler(_: Request, exception: BaseException):
    return JSONResponse(
        ExceptionModel.model_validate(exception).model_dump(),
        exception.code if exception.code in HTTPStatus else HTTPStatus.OK,
        {"X-DOAXVV-Status": str(exception.code)},
    )


def main():
    run(app)


if __name__ == "__main__":
    main()
