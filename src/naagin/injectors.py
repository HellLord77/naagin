from fastapi import Depends
from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession

from naagin.providers import provide_session
from naagin.providers import provide_session_
from naagin.types.cookies import PINKSIDCookie
from naagin.types.headers import AccessTokenHeader
from naagin.utils import should_endec


async def inject_session_key(
    access_token: AccessTokenHeader,
    pinksid: PINKSIDCookie,
    request: Request,
    session: AsyncSession = Depends(provide_session),
):
    if should_endec(request.scope):
        session_ = await provide_session_(access_token, pinksid, session)
        request.state.session_key = session_.session_key
