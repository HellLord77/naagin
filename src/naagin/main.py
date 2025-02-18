from collections import defaultdict
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
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


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None]:
    logger.setLevel(settings.logging.level)
    handler = RichHandler(markup=True, rich_tracebacks=True)
    formatter = Formatter("[underline]%(name)s[/underline] %(message)s", "[%X]")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    sqlalchemy_logger = getLogger("sqlalchemy.engine.Engine")
    sqlalchemy_handler = SQLAlchemyHandler(show_path=False)
    sqlalchemy_logger.addHandler(sqlalchemy_handler)

    if settings.logging.duplicate_model and logger.isEnabledFor(WARNING):
        model_map = defaultdict(list)
        for model in ModelBase.__subclasses__():
            annotations = frozenset(model.__annotations__.items())
            if len(annotations) >= settings.logging.duplicate_model_length:
                model_map[annotations].append(model)

        for models in model_map.values():
            if len(models) > 1:
                message = "Possible duplicate models:"
                for model in models:
                    path = getfile(model)
                    lines, lineno = getsourcelines(model)
                    link = AsyncPath(path).as_uri()
                    message += f"\n[link={link}]{path}[/link]:[link={link}#{lineno}]{lineno}[/link]"
                    message += f"\n    {lines[0].rstrip()}"
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
            middleware=Middleware(AESMiddleware, send_encoded=settings.api.encrypt, session=settings.database.session),
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
app.add_exception_handler(RequestValidationError, InvalidParameterException.handler)
app.add_exception_handler(StarletteHTTPException, InternalServerErrorException.handler)
app.add_exception_handler(ExceptionBase, ExceptionBase.handler)

app.include_router(routers.api.router, tags=["api"])
app.include_router(routers.api01.router, tags=["api01"])
