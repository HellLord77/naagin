from base64 import b64decode

from fastapi import Request

from naagin import settings
from naagin.enums import EncodingEnum
from naagin.providers import provide_session_cached
from naagin.utils import request_decompress_body
from naagin.utils import request_decrypt_body
from naagin.utils import request_headers
from .utils import should_endec


async def decode_body(request: Request, call_next):
    if await request.body() and should_endec(request):
        headers = request_headers(request)

        encrypted = headers.get("X-DOAXVV-Encrypted")
        if encrypted is not None:
            session = await provide_session_cached(
                request, session=settings.database.session
            )
            await request_decrypt_body(
                request, session.session_key, b64decode(encrypted)
            )

        encoding = headers.get("X-DOAXVV-Encoding")
        if encoding == EncodingEnum.DEFLATE:
            await request_decompress_body(request)

        headers["Content-Type"] = "application/json"
    return await call_next(request)
