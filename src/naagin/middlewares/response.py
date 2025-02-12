from http import HTTPStatus

from fastapi import Request
from fastapi import Response
from starlette.middleware.base import RequestResponseEndpoint
from starlette.middleware.base import _StreamingResponse

from naagin import settings
from naagin.providers import provide_session_cached
from naagin.utils import response_compress_body
from naagin.utils import response_encrypt_body


async def compress_body(request: Request, call_next: RequestResponseEndpoint) -> Response:
    response = await call_next(request)
    if response.status_code == HTTPStatus.OK:
        if not isinstance(response, _StreamingResponse):
            raise NotImplementedError

        response_compress_body(response)
    return response


async def encrypt_body(request: Request, call_next: RequestResponseEndpoint) -> Response:
    response = await call_next(request)
    if response.status_code == HTTPStatus.OK:
        if not isinstance(response, _StreamingResponse):
            raise NotImplementedError

        session = await provide_session_cached(request, session=settings.database.session)
        response_encrypt_body(response, session.session_key)
    return response
