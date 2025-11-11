from collections.abc import AsyncGenerator

from fastapi import Depends
from fastapi import Request
from sqlalchemy import func

from naagin import settings
from naagin.classes import AsyncSession
from naagin.decorators import async_req_cache  # noqa: TID251
from naagin.exceptions import AuthenticationFailedException
from naagin.schemas import MaintenanceSchema
from naagin.schemas import SessionSchema
from naagin.types_.securities import CookieSecurity
from naagin.types_.securities import HeaderSecurity


async def provide_database() -> AsyncGenerator[AsyncSession]:
    database = settings.database.sessionmaker()
    try:
        yield database
    except Exception:
        await database.rollback()
        raise
    else:
        await database.commit()
    finally:
        await database.close()


async def provide_maintenance(database: AsyncSession = Depends(provide_database)) -> MaintenanceSchema | None:
    maintenance = await database.find(
        MaintenanceSchema, func.current_timestamp().between(MaintenanceSchema.started_at, MaintenanceSchema.end_at)
    )
    if maintenance is not None:
        database.expunge(maintenance)
    return maintenance


@async_req_cache
async def provide_session(
    request: Request,
    access_token: HeaderSecurity = None,
    pinksid: CookieSecurity = None,
    database: AsyncSession = Depends(provide_database),
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

    session = await database.find(SessionSchema, whereclause)
    if session is None:
        raise AuthenticationFailedException
    database.expunge(session)
    return session


async def provide_owner_id(session: SessionSchema = Depends(provide_session)) -> int:
    return session.owner_id
