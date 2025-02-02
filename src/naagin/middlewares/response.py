from http import HTTPStatus

from fastapi import Request

from naagin import settings
from naagin.providers import provide_session_cached
from naagin.utils import response_compress_body
from naagin.utils import response_encrypt_body
from .utils import should_endec


async def encode_body(request: Request, call_next):
    response = await call_next(request)
    if response.status_code == HTTPStatus.OK and should_endec(request):
        if not hasattr(response, "body_iterator"):
            raise NotImplementedError

        if settings.api.compress:
            response_compress_body(response)
        if settings.api.encrypt:
            session = await provide_session_cached(
                request, session=settings.database.session
            )
            response_encrypt_body(response, session.session_key)
    return response
