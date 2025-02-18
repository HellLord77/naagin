from fastapi import APIRouter

from naagin.models.api import RoomGirlsPostRequestModel
from naagin.models.api import RoomGirlsPostResponseModel
from naagin.schemas import OwnerRoomSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency

router = APIRouter(prefix="/girls")


@router.post("")
async def post(
    request: RoomGirlsPostRequestModel, session: SessionDependency, owner_id: OwnerIdDependency
) -> RoomGirlsPostResponseModel:
    owner_room = await session.get_one(OwnerRoomSchema, owner_id)

    owner_room.main_girl_mid = request.main_girl_mid
    owner_room.sub_girl_mid = request.sub_girl_mid

    await session.flush()

    return RoomGirlsPostResponseModel(owner_room=owner_room)
