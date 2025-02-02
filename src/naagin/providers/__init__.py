from typing import AsyncGenerator
from typing import Optional

from fastapi import Depends
from fastapi import Request
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from naagin import settings
from naagin.exceptions import AuthenticationFailedException
from naagin.schemas import SessionSchema
from naagin.types.cookies import PINKSIDCookie
from naagin.types.headers import AccessTokenHeader
from . import csv


async def provide_session() -> AsyncGenerator[AsyncSession]:
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


async def provide_session_cached(
    request: Request,
    access_token: Optional[AccessTokenHeader] = None,
    pinksid: PINKSIDCookie = None,
    session: AsyncSession = Depends(provide_session),
) -> SessionSchema:
    state = request.state
    if not hasattr(state, "session"):
        if access_token is None:
            access_token = request.headers["X-DOAXVV-Access-Token"]
        if pinksid is None:
            pinksid = request.cookies.get("PINKSID")

        if access_token != "XPEACHACCESSTOKEN":
            whereclause = SessionSchema.access_token == access_token
        elif pinksid is not None:
            whereclause = SessionSchema.pinksid == pinksid
        else:
            raise AuthenticationFailedException

        session_ = await session.scalar(select(SessionSchema).where(whereclause))
        if session_ is None:
            raise AuthenticationFailedException
        session.expunge(session_)
        state.session = session_
    return state.session


async def provide_owner_id(
    session: SessionSchema = Depends(provide_session_cached),
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
