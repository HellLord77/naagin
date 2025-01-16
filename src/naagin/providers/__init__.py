from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.ext.asyncio import AsyncSession

from naagin import settings
from naagin.schemas import OptionItemAutoLockSchema
from naagin.schemas import OwnerSchema
from naagin.schemas import TutorialSchema
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
            raise HTTPException(status.HTTP_401_UNAUTHORIZED)
    else:
        if access_token is None:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED)

    owner_id = int(access_token)
    owner = await session.get(OwnerSchema, owner_id)
    if owner is None:
        owner = OwnerSchema(owner_id=owner_id)
        session.add(owner)
        await session.flush()

        tutorial = TutorialSchema(owner_id=owner_id, event_mid=0)
        option_item_auto_lock = OptionItemAutoLockSchema(owner_id=owner_id)
        session.add(tutorial)
        session.add(option_item_auto_lock)
        await session.flush()
    return owner_id
