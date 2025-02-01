from base64 import b64decode

from fastapi import Request

from naagin.enums import EncodingEnum
from naagin.utils import get_session_key
from naagin.utils import request_decompress_body
from naagin.utils import request_decrypt_body
from naagin.utils import request_headers
from naagin.utils import should_endec


async def decode_body(request: Request, call_next):
    if await request.body() and should_endec(request):
        headers = request_headers(request)

        encrypted = headers.get("X-DOAXVV-Encrypted")
        if encrypted is not None:
            session_key = await get_session_key(request)
            await request_decrypt_body(request, session_key, b64decode(encrypted))

        encoding = headers.get("X-DOAXVV-Encoding")
        if encoding == EncodingEnum.DEFLATE:
            await request_decompress_body(request)

        headers["Content-Type"] = "application/json"
    return await call_next(request)
