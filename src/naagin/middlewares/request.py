from base64 import b64decode

from fastapi import Request
from fastapi import Response
from starlette.middleware.base import RequestResponseEndpoint

from naagin import settings
from naagin.enums import EncodingEnum
from naagin.providers import provide_session_
from naagin.utils import request_decompress_body
from naagin.utils import request_decrypt_body


async def decompress_body(request: Request, call_next: RequestResponseEndpoint) -> Response:
    if await request.body():
        encoding = request.headers.get("X-DOAXVV-Encoding")

        if encoding == EncodingEnum.DEFLATE:
            await request_decompress_body(request)

    return await call_next(request)


async def decrypt_body(request: Request, call_next: RequestResponseEndpoint) -> Response:
    if await request.body():
        encrypted = request.headers.get("X-DOAXVV-Encrypted")

        if encrypted is not None:
            session = await provide_session_(request, session=settings.database.session)
            initialization_vector = b64decode(encrypted)
            await request_decrypt_body(request, session.session_key, initialization_vector)

    return await call_next(request)
