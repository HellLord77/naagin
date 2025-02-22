from base64 import b64encode
from collections import defaultdict
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from datetime import datetime
from http import HTTPStatus
from inspect import getfile
from inspect import getsourcelines
from json import JSONDecodeError
from logging import WARNING
from logging import Formatter
from logging import getLogger
from time import perf_counter

from aiopath import AsyncPath
from fastapi import FastAPI
from fastapi import Request
from fastapi import Response
from fastapi.exceptions import RequestValidationError
from fastapi.exceptions import StarletteHTTPException
from fastapi.middleware import Middleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import ORJSONResponse
from orjson import loads
from rich.logging import RichHandler
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.base import RequestResponseEndpoint

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
from .exceptions import UnderMaintenanceNowException
from .filters import encoding_filter
from .filters import gzip_filter
from .middlewares import AESMiddleware
from .middlewares import DeflateMiddleware
from .middlewares import FilteredMiddleware
from .middlewares import LimitingBodyRequestMiddleware
from .middlewares import RenewedMiddleware
from .middlewares import StackedMiddleware
from .providers import provide_session
from .utils import SQLAlchemyHandler
from .utils import response_peek_body
from .utils.exception_handlers import not_found_handler


def format_model_log(model: type[ModelBase]) -> str:
    path = getfile(model)
    link = AsyncPath(path).as_uri()
    lines, lineno = getsourcelines(model)

    message = f"\n[link={link}]{path}[/link]:[link={link}#{lineno}]{lineno}[/link]"
    message += f"\n    {lines[0].rstrip()}"
    return message


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None]:  # noqa: C901
    loggers.app.setLevel(settings.logging.level)
    handler = RichHandler(markup=True, rich_tracebacks=True)
    formatter = Formatter("[code]%(name)s[/code] %(message)s", "[%X]")
    handler.setFormatter(formatter)
    loggers.app.addHandler(handler)

    sqlalchemy_logger = getLogger("sqlalchemy.engine.Engine")
    sqlalchemy_handler = SQLAlchemyHandler(show_path=False)
    sqlalchemy_logger.handlers = [sqlalchemy_handler]

    if settings.logging.model and loggers.model.isEnabledFor(WARNING):
        optional_datetime = datetime | None
        for model in ModelBase.__subclasses__():
            for name, type_ in model.__annotations__.items():
                if name == "updated_at" and type_ != optional_datetime:
                    message = "Wrong `updated_at` annotation:"
                    message += format_model_log(model)
                    loggers.model.warning(message)

        for model in ModelBase.__subclasses__():
            json_schema_extra = model.model_config.get("json_schema_extra", None)
            if json_schema_extra is not None:
                message = "Unnecessary `json_schema_extra` config:"
                message += format_model_log(model)
                loggers.model.warning(message)

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
                loggers.model.warning(message)

    loggers.api.debug("Routes count: %d", len(routers.api.router.routes))
    loggers.api01.debug("Routes count: %d", len(routers.api01.router.routes))

    hooks.attach()

    async with settings.database.engine.begin() as connection:
        # await connection.run_sync(SchemaBase.metadata.drop_all)
        await connection.run_sync(SchemaBase.metadata.create_all)

    yield

    await settings.database.engine.dispose()


kwargs = {}
if not settings.fastapi.swagger_ui:
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


async def add_debug_headers(request: Request, call_next: RequestResponseEndpoint) -> Response:
    headers = {}
    try:
        session = await provide_session(request, database=settings.database.session)
    except ExceptionBase:
        pass
    else:
        headers["X-Session-Key"] = b64encode(session.key).decode()

        request_body = await request.body()
        if request_body:
            try:
                await request.json()
            except JSONDecodeError:
                pass
            else:
                headers["X-Request"] = request_body.decode()

    response = await call_next(request)
    response_body = await response_peek_body(response)
    if response_body:
        try:
            loads(response_body)
        except JSONDecodeError:
            pass
        else:
            headers["X-Response"] = response_body.decode()
    response.headers.update(headers)

    return response


middlewares = [
    Middleware(
        RenewedMiddleware,
        middleware=Middleware(
            DeflateMiddleware, send_encoded=settings.api.compress, compress_level=settings.api.compress_level
        ),
    ),
    Middleware(
        RenewedMiddleware,
        middleware=Middleware(AESMiddleware, send_encoded=settings.api.encrypt, database=settings.database.session),
    ),
]
if settings.fastapi.debug_headers:
    middlewares.insert(0, Middleware(BaseHTTPMiddleware, dispatch=add_debug_headers))

app.add_middleware(FilteredMiddleware, middleware=Middleware(StackedMiddleware, *middlewares), filter=encoding_filter)

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

if settings.fastapi.debug_headers:

    @app.middleware("http")
    async def add_process_time_header(request: Request, call_next: RequestResponseEndpoint) -> Response:
        start_time = perf_counter()
        response = await call_next(request)
        process_time = perf_counter() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        return response
