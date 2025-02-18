from fastapi import APIRouter

from naagin.models.api import RoomPostResponseModel
from naagin.schemas import OwnerRoomSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency

from . import girl

router = APIRouter(prefix="/room")

router.include_router(girl.router)


@router.post("")
async def post(session: SessionDependency, owner_id: OwnerIdDependency) -> RoomPostResponseModel:
    owner_room = await session.get(OwnerRoomSchema, owner_id)

    if owner_room is None:
        owner_room = OwnerRoomSchema(owner_id=owner_id)

        await session.add(owner_room)
        await session.flush()

    return RoomPostResponseModel(owner_room=owner_room)
