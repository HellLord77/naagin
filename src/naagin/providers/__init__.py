from base64 import b64decode

from fastapi import Depends
from fastapi import Request
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from naagin import settings
from naagin.enums import EncodingEnum
from naagin.exceptions import AuthenticationFailedException
from naagin.schemas import SessionSchema
from naagin.types.cookies import PINKSIDCookie
from naagin.types.headers import AccessTokenHeader
from naagin.types.headers import ContentLengthHeader
from naagin.types.headers import ContentTypeHeader
from naagin.types.headers import EncodingHeader
from naagin.types.headers import EncryptedHeader
from naagin.utils import request_decompress_body
from naagin.utils import request_decrypt_body
from . import csv


async def provide_session() -> AsyncSession:
    session = settings.database.sessionmaker()
    try:
        yield session
    except Exception:
        await session.rollback()
        raise
    else:
        await session.commit()
    finally:
        await session.close()


async def provide_session_(
    access_token: AccessTokenHeader,
    pinksid: PINKSIDCookie,
    session: AsyncSession = Depends(provide_session),
) -> SessionSchema:
    if access_token and access_token != "XPEACHACCESSTOKEN":
        whereclause = SessionSchema.access_token == access_token
    elif pinksid is not None:
        whereclause = SessionSchema.pinksid == pinksid
    else:
        raise AuthenticationFailedException

    session_ = await session.scalar(select(SessionSchema).where(whereclause))
    if session_ is None:
        raise AuthenticationFailedException
    return session_


async def provide_owner_id(
    session: SessionSchema = Depends(provide_session_),
) -> int:
    return session.owner_id

    # owner_id = int(access_token)
    # owner = await session.get(OwnerSchema, owner_id)
    # if owner is None:
    #     owner = OwnerSchema(owner_id=owner_id)
    #     session.add(owner)
    #     await session.flush()
    #
    #     wallet = WalletSchema(owner_id=owner_id)
    #     session.add(wallet)
    #     await session.flush()
    # return owner_id


async def provide_request_body(
    content_type: ContentTypeHeader,
    content_length: ContentLengthHeader,
    access_token: AccessTokenHeader,
    encoding: EncodingHeader,
    encrypted: EncryptedHeader,
    pinksid: PINKSIDCookie,
    request: Request,
    session: AsyncSession = Depends(provide_session),
):
    if not request.url.path.removeprefix("/api/v1").startswith("/session"):
        if content_type == "application/octet-stream" and content_length:
            session_ = await provide_session_(access_token, pinksid, session)
            await request_decrypt_body(
                request, session_.session_key, b64decode(encrypted)
            )
            if encoding == EncodingEnum.DEFLATE:
                await request_decompress_body(request)
