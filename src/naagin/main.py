from collections import defaultdict
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from datetime import datetime
from http import HTTPStatus
from inspect import getfile
from inspect import getsourcelines
from logging import WARNING
from logging import Formatter
from logging import getLogger

from aiopath import AsyncPath
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.exceptions import StarletteHTTPException
from fastapi.middleware import Middleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import ORJSONResponse
from rich.logging import RichHandler

from . import __version__
from . import apps
from . import hooks
from . import routers
from . import settings
from .bases import ExceptionBase
from .bases import ModelBase
from .bases import SchemaBase
from .exceptions import InternalServerErrorException
from .exceptions import InvalidParameterException
from .exceptions import MethodNotAllowedException
from .exceptions import UnderMaintenanceNowException
from .filters import encoding_filter
from .filters import gzip_filter
from .middlewares import AESMiddleware
from .middlewares import DeflateMiddleware
from .middlewares import FilteredMiddleware
from .middlewares import LimitingBodyRequestMiddleware
from .middlewares import RenewedMiddleware
from .middlewares import StackedMiddleware
from .utils import SQLAlchemyHandler
from .utils.exception_handlers import not_found_handler

logger = settings.logging.logger


def format_model_log(model: type[ModelBase]) -> str:
    path = getfile(model)
    link = AsyncPath(path).as_uri()
    lines, lineno = getsourcelines(model)
    message = f"\n[link={link}]{path}[/link]:[link={link}#{lineno}]{lineno}[/link]"
    message += f"\n    {lines[0].rstrip()}"
    return message


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None]:  # noqa: C901
    logger.setLevel(settings.logging.level)
    handler = RichHandler(markup=True, rich_tracebacks=True)
    formatter = Formatter("[underline]%(name)s[/underline] %(message)s", "[%X]")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    sqlalchemy_logger = getLogger("sqlalchemy.engine.Engine")
    sqlalchemy_handler = SQLAlchemyHandler(show_path=False)
    sqlalchemy_logger.addHandler(sqlalchemy_handler)

    if logger.isEnabledFor(WARNING):
        if settings.logging.model_type:
            optional_datetime = datetime | None
            for model in ModelBase.__subclasses__():
                for name, type_ in model.__annotations__.items():
                    if name == "updated_at" and type_ != optional_datetime:
                        message = "Possible wrong `update_at` annotation:"
                        message += format_model_log(model)
                        logger.warning(message)

        if settings.logging.model_dup:
            model_map = defaultdict(list)
            for model in ModelBase.__subclasses__():
                annotations = frozenset(model.__annotations__.items())
                if len(annotations) >= settings.logging.model_dup_len:
                    model_map[annotations].append(model)

            for models in model_map.values():
                if len(models) > 1:
                    message = "Possible duplicate models:"
                    for model in models:
                        message += format_model_log(model)
                    logger.warning(message)

    hooks.attach()

    async with settings.database.engine.begin() as connection:
        # await connection.run_sync(SchemaBase.metadata.drop_all)
        await connection.run_sync(SchemaBase.metadata.create_all)

    yield

    await settings.database.engine.dispose()


kwargs = {}
if not settings.fastapi.swagger:
    kwargs["openapi_url"] = None
    kwargs["docs_url"] = None

app = FastAPI(
    title="naagin",
    version=__version__,
    redoc_url=None,
    lifespan=lifespan,
    default_response_class=ORJSONResponse,
    **kwargs,
)

app.mount("/game", apps.game.app)

app.add_middleware(
    FilteredMiddleware,
    middleware=Middleware(
        StackedMiddleware,
        Middleware(
            RenewedMiddleware,
            middleware=Middleware(
                DeflateMiddleware, send_encoded=settings.api.compress, compress_level=settings.api.compress_level
            ),
        ),
        Middleware(
            RenewedMiddleware,
            middleware=Middleware(
                AESMiddleware, send_encoded=settings.api.encrypt, database=settings.database.database
            ),
        ),
    ),
    filter=encoding_filter,
)
if settings.fastapi.limit:
    app.add_middleware(
        RenewedMiddleware,
        middleware=Middleware(LimitingBodyRequestMiddleware, maximum_size=settings.fastapi.limit_max_size),
    )
if settings.fastapi.gzip:
    app.add_middleware(
        FilteredMiddleware,
        middleware=Middleware(GZipMiddleware, settings.fastapi.gzip_min_size, settings.fastapi.gzip_compress_level),
        filter=gzip_filter,
    )

app.add_exception_handler(HTTPStatus.NOT_FOUND, not_found_handler)
app.add_exception_handler(HTTPStatus.METHOD_NOT_ALLOWED, MethodNotAllowedException.handler)
app.add_exception_handler(HTTPStatus.INTERNAL_SERVER_ERROR, InternalServerErrorException.handler)
app.add_exception_handler(HTTPStatus.SERVICE_UNAVAILABLE, UnderMaintenanceNowException.handler)
app.add_exception_handler(RequestValidationError, InvalidParameterException.handler)
app.add_exception_handler(StarletteHTTPException, InternalServerErrorException.handler)
app.add_exception_handler(ExceptionBase, ExceptionBase.handler)

app.include_router(routers.api.router, tags=["api"])
app.include_router(routers.api01.router, tags=["api01"])
