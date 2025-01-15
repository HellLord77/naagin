from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.ext.asyncio import AsyncSession

from . import csv
from .. import settings
from ..schemas import OwnerSchema
from ..schemas import TutorialSchema
from ..types.cookies import PINKSIDCookie
from ..types.headers import AccessTokenHeader


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
            raise HTTPException(status.HTTP_401_UNAUTHORIZED)
    else:
        if access_token is None:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED)

    owner_id = int(access_token)
    owner = await session.get(OwnerSchema, owner_id)
    if owner is None:
        owner = OwnerSchema(owner_id=owner_id)
        tutorial = TutorialSchema(owner_id=owner_id, event_mid=0)
        session.add(owner)
        session.add(tutorial)
        await session.flush()
    return owner_id
