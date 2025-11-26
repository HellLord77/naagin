from collections import defaultdict
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from datetime import datetime
from http import HTTPStatus
from importlib.util import find_spec
from inspect import get_annotations
from inspect import getfile
from inspect import getsourcelines
from itertools import islice
from logging import Formatter
from logging import getLogger
from sys import modules

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.exceptions import StarletteHTTPException
from fastapi.middleware import Middleware
from fastapi.middleware.gzip import GZipMiddleware
from rich.logging import RichHandler
from starlette.middleware.base import BaseHTTPMiddleware

from naagin.imports import AsyncPath
from naagin.imports import JSONResponse

from . import __version__
from . import apps
from . import hooks
from . import loggers
from . import routers
from . import settings
from .bases import ExceptionBase
from .bases import ModelBase
from .bases import SchemaBase
from .exceptions import InternalServerErrorException
from .exceptions import InvalidParameterException
from .exceptions import MethodNotAllowedException
from .exceptions import NotFoundException
from .exceptions import UnderMaintenanceNowException
from .filters import encoding_filter
from .filters import gzip_filter
from .middlewares import AESMiddleware
from .middlewares import DeflateMiddleware
from .middlewares import FilteredMiddleware
from .middlewares import LimitingBodyRequestMiddleware
from .middlewares import RenewedMiddleware
from .middlewares import StackedMiddleware
from .middlewares import add_debug_headers
from .middlewares import add_process_time_header
from .middlewares import remove_version_headers
from .utils import SQLAlchemyHandler


def setup_sqlalchemy_logger() -> None:
    logger = getLogger("sqlalchemy.engine.Engine")
    handler = SQLAlchemyHandler(show_path=False)
    logger.handlers = [handler]


def setup_logging() -> None:
    loggers.app.setLevel(settings.logging.level)
    handler = RichHandler(show_path=False, markup=True, rich_tracebacks=True)
    formatter = Formatter("[code]%(name)s[/code] %(message)s", "[%X]")
    handler.setFormatter(formatter)
    loggers.app.addHandler(handler)

    setup_sqlalchemy_logger()


def format_model_log(model: type[ModelBase]) -> str:
    path = getfile(model)
    link = AsyncPath(path).as_uri()
    lines, lineno = getsourcelines(model)

    message = f"\n[link={link}]{path}[/link]:[link={link}#{lineno}]{lineno}[/link]"
    message += f"\n    {lines[0].rstrip()}"
    return message


def log_model() -> None:
    annotation_map = {"created_at": datetime, "updated_at": datetime | None}
    for model in ModelBase.__subclasses__():
        annotations = get_annotations(model)
        for field, annotation in annotation_map.items():
            if annotations.get(field, annotation) != annotation:
                message = f"Wrong model field [bold]{field}[/bold] annotation:"
                message += format_model_log(model)
                loggers.model.error(message)

    model_map = defaultdict(list)
    for model in ModelBase.__subclasses__():
        json_schema_extra = model.model_config.get("json_schema_extra", None)
        if json_schema_extra is not None:
            message = "Unnecessary model config [bold]json_schema_extra[/bold] found:"
            message += format_model_log(model)
            loggers.model.warning(message)

        annotations = frozenset(get_annotations(model).items())
        if len(annotations) >= settings.logging.model_duplicate_length:
            model_map[annotations].append(model)

    for models in model_map.values():
        if len(models) > 1:
            message = "Possible duplicate model found:"
            for model in models:
                message += format_model_log(model)
            loggers.model.warning(message)


def log_route() -> None:
    router_names = [name for name in modules if name.startswith(routers.__name__)]
    router_names.sort()

    for index, router_name in enumerate(router_names, 1):
        if any(name.startswith(router_name) for name in islice(router_names, index, None)):
            continue

        router = modules[router_name]
        if AsyncPath(router.__file__).name == "__init__.py":
            loggers.route.warning("Unnecessary module [bold]%s[/bold] found", router_name)


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None]:
    setup_logging()

    if find_spec("httptools") is not None:
        loggers.app.error("Conflicting module [bold]httptools[/bold] found")

    if settings.environment.file is not None:
        loggers.setting.debug("Unused cli arg [bold]--env-file[/bold]")

    if settings.app.limit_request:
        loggers.setting.debug("Unused cli arg [bold]--limit-request-line[/bold]")

    loggers.setting.info("environment: %s", settings.environment)
    loggers.setting.info("logging: %s", settings.logging)
    loggers.setting.info("app: %s", settings.app)

    loggers.setting.info("version: %s", settings.version)
    loggers.setting.info("data: %s", settings.data)
    loggers.setting.info("database: %s", settings.database)

    loggers.setting.info("api: %s", settings.api)
    loggers.setting.info("api01: %s", settings.api01)

    loggers.setting.info("game: %s", settings.game)
    loggers.setting.info("cdn01: %s", settings.cdn01)
    loggers.setting.info("www: %s", settings.www)

    if settings.logging.model:
        log_model()

    if settings.logging.route:
        log_route()

    loggers.api.debug("Routes count: %d", len(routers.api.router.routes))
    loggers.api01.debug("Routes count: %d", len(routers.api01.router.routes))

    hooks.attach()

    async with settings.database.engine.begin() as connection:
        # await connection.run_sync(SchemaBase.metadata.drop_all)
        await connection.run_sync(SchemaBase.metadata.create_all)

    yield

    await settings.database.engine.dispose()


kwargs = {}
if not settings.app.swagger_ui:
    kwargs["openapi_url"] = None
    kwargs["docs_url"] = None

app = FastAPI(
    title="naagin",
    version=__version__,
    redoc_url=None,
    lifespan=lifespan,
    default_response_class=JSONResponse,
    **kwargs,
)

app.mount("/game", apps.game.app)
app.mount("/cdn01", apps.cdn01.app)
app.mount("/www", apps.www.app)

middlewares = [
    Middleware(
        RenewedMiddleware,
        middleware=Middleware(
            DeflateMiddleware, send_encoded=settings.api.compress_enabled, compress_level=settings.api.compress_level
        ),
    ),
    Middleware(
        RenewedMiddleware,
        middleware=Middleware(
            AESMiddleware, send_encoded=settings.api.encrypt_enabled, database=settings.database.session
        ),
    ),
]
if settings.app.debug_headers:
    middlewares.insert(0, Middleware(BaseHTTPMiddleware, dispatch=add_debug_headers))
app.add_middleware(FilteredMiddleware, middleware=Middleware(StackedMiddleware, *middlewares), filter=encoding_filter)

if settings.app.limit_request:
    app.add_middleware(
        RenewedMiddleware,
        middleware=Middleware(LimitingBodyRequestMiddleware, maximum_size=settings.app.limit_maximum_size),
    )

if settings.app.gzip_response:
    app.add_middleware(
        FilteredMiddleware,
        middleware=Middleware(GZipMiddleware, settings.app.gzip_minimum_size, settings.app.gzip_compress_level),
        filter=gzip_filter,
    )

if settings.version.strict:
    app.add_middleware(BaseHTTPMiddleware, dispatch=remove_version_headers)

app.add_middleware(BaseHTTPMiddleware, dispatch=add_process_time_header)

app.add_exception_handler(HTTPStatus.NOT_FOUND, NotFoundException.handler)
app.add_exception_handler(HTTPStatus.METHOD_NOT_ALLOWED, MethodNotAllowedException.handler)
app.add_exception_handler(HTTPStatus.INTERNAL_SERVER_ERROR, InternalServerErrorException.handler)
app.add_exception_handler(HTTPStatus.SERVICE_UNAVAILABLE, UnderMaintenanceNowException.handler)
app.add_exception_handler(RequestValidationError, InvalidParameterException.handler)
app.add_exception_handler(StarletteHTTPException, InternalServerErrorException.handler)
app.add_exception_handler(ExceptionBase, ExceptionBase.handler)

app.include_router(routers.api.router, tags=["api"])
app.include_router(routers.api01.router, tags=["api01"])
