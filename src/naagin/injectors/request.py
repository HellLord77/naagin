from base64 import b64decode

from fastapi import Depends
from fastapi import Request

from naagin.enums import EncodingEnum
from naagin.providers import provide_session_
from naagin.schemas import SessionSchema
from naagin.types.headers import EncodingHeader
from naagin.types.headers import EncryptedHeader
from naagin.utils import request_decompress_body
from naagin.utils import request_decrypt_body


async def inject_session_key(
    request: Request,
    session: SessionSchema = Depends(provide_session_),
):
    request.state.session_key = session.session_key


async def inject_decoded_body(
    encoding: EncodingHeader,
    encrypted: EncryptedHeader,
    request: Request,
    session: SessionSchema = Depends(provide_session_),
):
    body = await request.body()
    if body:
        if encrypted is not None:
            await request_decrypt_body(
                request, session.session_key, b64decode(encrypted)
            )
        if encoding == EncodingEnum.DEFLATE:
            await request_decompress_body(request)
