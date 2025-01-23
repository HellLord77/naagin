from fastapi import APIRouter
from fastapi import Response

from naagin.models.api import SessionPostRequestModel
from naagin.models.api import SessionPostResponseModel
from naagin.schemas import OwnerSchema
from naagin.schemas import SessionSchema
from naagin.types.dependencies import SessionDependency
from naagin.utils import response_set_doaxvv_header
from . import key

router = APIRouter(prefix="/session")

router.include_router(key.router)


@router.post("")
async def post(
    _: SessionPostRequestModel, session: SessionDependency, response: Response
) -> SessionPostResponseModel:
    owner_id = 6957694
    owner = await session.get(OwnerSchema, owner_id)
    if owner is None:
        owner = OwnerSchema(owner_id=owner_id)
        session.add(owner)
        await session.flush()
        await session.refresh(owner)

    session_ = await session.get(SessionSchema, owner_id)
    if session_ is not None:
        await session.delete(session_)
        await session.flush()

    session_ = SessionSchema(owner_id=owner_id)
    session.add(session_)
    await session.flush()
    await session.refresh(session_)

    response_set_doaxvv_header(response, "Access-Token", session_.access_token)
    response.set_cookie("PINKSID", session_.pinksid, samesite=None)
    return SessionPostResponseModel(
        auth=True, owner_id=owner.owner_id, owner_status=owner.status
    )
