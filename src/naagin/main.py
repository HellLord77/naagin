from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from http import HTTPStatus
from inspect import getfile
from inspect import getsourcelines
from logging import Formatter
from logging import getLogger

from aiopath import AsyncPath
from fastapi import Depends
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.gzip import GZipMiddleware
from rich.logging import RichHandler

from . import __version__
from . import apps
from . import injectors
from . import middlewares
from . import routers
from . import settings
from .exceptions import InternalServerErrorException
from .exceptions import InvalidParameterException
from .exceptions import MethodNotAllowedException
from .exceptions.base import CustomBaseException
from .middlewares.common import FilterMiddleware
from .models.base import CustomBaseModel
from .schemas.base import CustomBaseSchema
from .utils import SQLAlchemyHandler
from .utils.exception_handlers import moved_permanently_handler
from .utils.exception_handlers import not_found_handler

logger = settings.logging.logger


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None]:
    logger.setLevel(settings.logging.level)
    handler = RichHandler(markup=True, rich_tracebacks=True)
    formatter = Formatter("%(message)s", datefmt="[%X]")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    sqlalchemy_logger = getLogger("sqlalchemy.engine.Engine")
    sqlalchemy_handler = SQLAlchemyHandler(show_path=False)
    sqlalchemy_logger.addHandler(sqlalchemy_handler)

    for models in CustomBaseModel.model_map.values():
        if len(models) > 1:
            message = "Possible duplicate models"
            for model in models:
                path = getfile(model)
                lines, lineno = getsourcelines(model)
                link = AsyncPath(path).as_uri()
                message += f"\n[link={link}]{path}[/link]:[link={link}#{lineno}]{lineno}[/link]"
                message += f"\n    {lines[0].rstrip()}"
            logger.warning(message)

    async with settings.database.engine.begin() as connection:
        # await connection.run_sync(BaseSchema.metadata.drop_all)
        await connection.run_sync(CustomBaseSchema.metadata.create_all)

    yield

    await settings.database.engine.dispose()


app = FastAPI(title="naagin", version=__version__, redoc_url=None, lifespan=lifespan)

app.mount("/game", apps.game.app)

app.add_middleware(FilterMiddleware, dispatch=middlewares.request.decompress_body, router=routers.api.router)
app.add_middleware(FilterMiddleware, dispatch=middlewares.request.decrypt_body, router=routers.api.router)
if settings.api.compress:
    app.add_middleware(FilterMiddleware, dispatch=middlewares.response.compress_body, router=routers.api.router)
if settings.api.encrypt:
    app.add_middleware(FilterMiddleware, dispatch=middlewares.response.encrypt_body, router=routers.api.router)
app.add_middleware(GZipMiddleware)

app.add_exception_handler(HTTPStatus.MOVED_PERMANENTLY, moved_permanently_handler)
app.add_exception_handler(HTTPStatus.NOT_FOUND, not_found_handler)
app.add_exception_handler(HTTPStatus.METHOD_NOT_ALLOWED, MethodNotAllowedException.handler)
app.add_exception_handler(HTTPStatus.INTERNAL_SERVER_ERROR, InternalServerErrorException.handler)
app.add_exception_handler(RequestValidationError, InvalidParameterException.handler)
app.add_exception_handler(CustomBaseException, CustomBaseException.handler)

app.include_router(routers.api.router, tags=["api"])
app.include_router(
    routers.api.v1.session.router,
    prefix="/api/v1",
    tags=["api", "session"],
    dependencies=[Depends(injectors.response.add_doaxvv_headers)],
)
app.include_router(routers.api01.router, tags=["api01"])
