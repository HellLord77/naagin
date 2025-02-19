from fastapi import APIRouter
from fastapi import Response

from naagin.models.api import SessionPostRequestModel
from naagin.models.api import SessionPostResponseModel
from naagin.schemas import OwnerSchema
from naagin.schemas import SessionSchema
from naagin.types.dependencies import DatabaseDependency
from naagin.utils import CustomHeader

from . import key

router = APIRouter(prefix="/session")

router.include_router(key.router)


@router.post("")
async def post(
    _: SessionPostRequestModel, database: DatabaseDependency, response: Response
) -> SessionPostResponseModel:
    owner_id = 6957694
    owner = await database.get(OwnerSchema, owner_id)
    if owner is None:
        owner = OwnerSchema(owner_id=owner_id)
        database.add(owner)

        await database.flush()
        await database.refresh(owner)

    session = await database.get(SessionSchema, owner_id)
    if session is not None:
        await database.delete(session)
        await database.flush()

    session = SessionSchema(owner_id=owner_id)
    database.add(session)

    await database.flush()
    await database.refresh(session)

    CustomHeader.set(response, "Access-Token", session.access_token)
    response.set_cookie("PINKSID", session.pinksid, samesite=None)
    return SessionPostResponseModel(auth=True, owner_id=owner.owner_id, owner_status=owner.status)
