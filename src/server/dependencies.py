from typing import Optional

from fastapi import Cookie
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Header
from fastapi import status
from sqlalchemy.ext.asyncio import AsyncSession

from . import settings
from .schemas import OwnerSchema
from .schemas import TutorialSchema


async def get_session() -> AsyncSession:
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


async def get_owner_id(
    x_doaxvv_access_token: Optional[str] = Header(None),
    pinksid: Optional[str] = Cookie(None),
    session: AsyncSession = Depends(get_session),
) -> int:
    if x_doaxvv_access_token == "XPEACHACCESSTOKEN":
        if pinksid is None:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED)
    else:
        if x_doaxvv_access_token is None:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED)

    owner_id = int(x_doaxvv_access_token)
    owner = await session.get(OwnerSchema, owner_id)
    if owner is None:
        owner = OwnerSchema(owner_id=owner_id)
        tutorial = TutorialSchema(owner_id=owner_id, event_mid=0)
        session.add(owner)
        session.add(tutorial)
        await session.flush()
    return owner_id
