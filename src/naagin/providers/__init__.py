from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from naagin import settings
from naagin.exceptions import AuthenticationFailedException
from naagin.schemas import OwnerSchema
from naagin.schemas import WalletSchema
from naagin.types.cookies import PINKSIDCookie
from naagin.types.headers import AccessTokenHeader
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


async def provide_owner_id(
    access_token: AccessTokenHeader,
    pinksid: PINKSIDCookie,
    session: AsyncSession = Depends(provide_session),
) -> int:
    if access_token == "XPEACHACCESSTOKEN":
        if pinksid is None:
            raise AuthenticationFailedException()
    else:
        if access_token is None:
            raise AuthenticationFailedException()

    owner_id = int(access_token)
    owner = await session.get(OwnerSchema, owner_id)
    if owner is None:
        owner = OwnerSchema(owner_id=owner_id)
        session.add(owner)
        await session.flush()

        wallet = WalletSchema(owner_id=owner_id)
        session.add(wallet)
        await session.flush()
    return owner_id
