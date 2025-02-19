from collections.abc import AsyncGenerator

from fastapi import Depends
from fastapi import Request
from sqlalchemy import func

from naagin import settings
from naagin.classes import AsyncSession
from naagin.decorators import async_request_cache_unsafe
from naagin.exceptions import AuthenticationFailedException
from naagin.schemas import MaintenanceSchema
from naagin.schemas import SessionSchema
from naagin.types.cookies import PINKSIDCookie
from naagin.types.headers import AccessTokenHeader


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


async def provide_maintenance(session: AsyncSession = Depends(provide_session)) -> MaintenanceSchema | None:
    maintenance = await session.find(
        MaintenanceSchema, func.current_timestamp().between(MaintenanceSchema.started_at, MaintenanceSchema.end_at)
    )
    if maintenance is not None:
        session.expunge(maintenance)
    return maintenance


@async_request_cache_unsafe
async def provide_session_(
    request: Request,
    access_token: AccessTokenHeader = None,
    pinksid: PINKSIDCookie = None,
    session: AsyncSession = Depends(provide_session),
) -> SessionSchema:
    if access_token is None:
        access_token = request.headers.get("X-DOAXVV-Access-Token")
    if pinksid is None:
        pinksid = request.cookies.get("PINKSID")

    if access_token is not None and access_token != "XPEACHACCESSTOKEN":  # noqa: S105
        whereclause = SessionSchema.access_token == access_token
    elif pinksid is not None:
        whereclause = SessionSchema.pinksid == pinksid
    else:
        raise AuthenticationFailedException

    session_ = await session.find(SessionSchema, whereclause)
    if session_ is None:
        raise AuthenticationFailedException
    session.expunge(session_)
    return session_


async def provide_owner_id(session: SessionSchema = Depends(provide_session_)) -> int:
    return session.owner_id
