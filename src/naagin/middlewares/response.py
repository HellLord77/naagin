from http import HTTPStatus

from fastapi import Request

from naagin import settings
from naagin.utils import response_compress_body
from naagin.utils import response_encrypt_body
from naagin.utils import should_endec


async def encode_body(request: Request, call_next):
    response = await call_next(request)
    if response.status_code == HTTPStatus.OK and should_endec(request):
        if not hasattr(response, "body_iterator"):
            raise NotImplementedError

        if settings.api.compress:
            response_compress_body(response)
        if settings.api.encrypt:
            response_encrypt_body(response, request.state.session_key)
    return response
