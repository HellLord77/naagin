from fastapi import Request

from naagin import settings
from naagin.utils import response_compress_body
from naagin.utils import response_encrypt_body
from naagin.utils import should_endec


async def encode_response_body_middleware(request: Request, call_next):
    response = await call_next(request)
    if should_endec(request.scope):
        if not hasattr(response, "body_iterator"):
            raise NotImplementedError

        if settings.api.compress:
            response_compress_body(response)
        if settings.api.encrypt:
            response_encrypt_body(response, request.state.session_key)
    return response
