from base64 import b64encode
from json import JSONDecodeError
from time import perf_counter

from fastapi import Request
from fastapi import Response
from orjson import loads
from starlette.datastructures import MutableHeaders
from starlette.middleware.base import RequestResponseEndpoint

from naagin import settings
from naagin.bases import ExceptionBase
from naagin.enums import DOAXVVHeaderEnum
from naagin.enums import NaaginHeaderEnum
from naagin.providers import provide_session
from naagin.utils import response_peek_body

from .aes import AESMiddleware as AESMiddleware
from .deflate import DeflateMiddleware as DeflateMiddleware
from .middleware.filtered import FilteredMiddleware as FilteredMiddleware
from .middleware.renewed import RenewedMiddleware as RenewedMiddleware
from .middleware.stacked import StackedMiddleware as StackedMiddleware
from .request.limiting_body import LimitingBodyRequestMiddleware as LimitingBodyRequestMiddleware


async def add_debug_headers(request: Request, call_next: RequestResponseEndpoint) -> Response:
    headers = {}
    try:
        session = await provide_session(request, database=settings.database.session)
    except ExceptionBase:
        pass
    else:
        headers[NaaginHeaderEnum.SESSION_KEY] = b64encode(session.key).decode()

        request_body = await request.body()
        if request_body:
            try:
                await request.json()
            except JSONDecodeError:
                pass
            else:
                headers[NaaginHeaderEnum.REQUEST_BODY] = request_body.decode()

    response = await call_next(request)
    response_body = await response_peek_body(response)
    if response_body:
        try:
            loads(response_body)
        except JSONDecodeError:
            pass
        else:
            headers[NaaginHeaderEnum.RESPONSE_BODY] = response_body.decode()
    response.headers.update(headers)

    return response


async def remove_version_headers(request: Request, call_next: RequestResponseEndpoint) -> Response:
    headers = MutableHeaders(raw=request.scope["headers"])
    del headers[DOAXVVHeaderEnum.APPLICATION_VERSION]
    del headers[DOAXVVHeaderEnum.MASTER_VERSION]
    del headers[DOAXVVHeaderEnum.RESOURCE_VERSION]
    return await call_next(request)


async def add_process_time_header(request: Request, call_next: RequestResponseEndpoint) -> Response:
    start_time = perf_counter()
    response = await call_next(request)
    process_time = perf_counter() - start_time
    response.headers[NaaginHeaderEnum.PROCESS_TIME] = str(process_time)
    return response
