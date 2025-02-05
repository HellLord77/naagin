from contextlib import asynccontextmanager
from http import HTTPStatus
from logging import getLogger
from typing import AsyncGenerator

from fastapi import Depends
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.gzip import GZipMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

from . import __version__
from . import apps
from . import injectors
from . import middlewares
from . import routers
from . import settings
from .exceptions import InternalServerErrorException
from .exceptions import InvalidParameterException
from .exceptions import MethodNotAllowedException
from .exceptions.base import BaseException
from .schemas.base import BaseSchema
from .utils import SQLAlchemyHandler
from .utils.exception_handlers import moved_permanently_handler
from .utils.exception_handlers import not_found_handler


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None]:
    logger = getLogger("sqlalchemy.engine.Engine")
    handler = SQLAlchemyHandler(show_path=False)
    logger.addHandler(handler)

    async with settings.database.engine.begin() as connection:
        # await connection.run_sync(BaseSchema.metadata.drop_all)
        await connection.run_sync(BaseSchema.metadata.create_all)

    yield

    await settings.database.engine.dispose()


app = FastAPI(title="naagin", version=__version__, lifespan=lifespan)

app.mount("/game", apps.game.app)

app.add_middleware(BaseHTTPMiddleware, dispatch=middlewares.request.decode_body)
app.add_middleware(BaseHTTPMiddleware, dispatch=middlewares.response.encode_body)
app.add_middleware(GZipMiddleware)

app.add_exception_handler(HTTPStatus.MOVED_PERMANENTLY, moved_permanently_handler)
app.add_exception_handler(HTTPStatus.NOT_FOUND, not_found_handler)
app.add_exception_handler(
    HTTPStatus.METHOD_NOT_ALLOWED, MethodNotAllowedException.handler
)
app.add_exception_handler(
    HTTPStatus.INTERNAL_SERVER_ERROR, InternalServerErrorException.handler
)
app.add_exception_handler(RequestValidationError, InvalidParameterException.handler)
app.add_exception_handler(BaseException, BaseException.handler)

app.include_router(routers.api.router, tags=["api"])
app.include_router(
    routers.api.v1.session.router,
    prefix="/api/v1",
    tags=["api", "session"],
    dependencies=[Depends(injectors.response.add_doaxvv_headers)],
)
app.include_router(routers.api01.router, tags=["api01"])
