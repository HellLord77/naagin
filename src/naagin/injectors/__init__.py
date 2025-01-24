from fastapi import Depends
from fastapi import Request

from naagin.providers import provide_session_
from naagin.schemas import SessionSchema


async def inject_session_key(
    request: Request,
    session: SessionSchema = Depends(provide_session_),
):
    request.state.session_key = session.session_key
