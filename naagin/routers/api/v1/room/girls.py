from fastapi import APIRouter

from naagin.models.api import RoomGirlsPostRequestModel
from naagin.models.api import RoomGirlsPostResponseModel
from naagin.schemas import OwnerRoomSchema
from naagin.types_.dependencies import DatabaseDependency
from naagin.types_.dependencies import OwnerIdDependency

router = APIRouter(prefix="/girls")


@router.post("")
async def post(
    request: RoomGirlsPostRequestModel, database: DatabaseDependency, owner_id: OwnerIdDependency
) -> RoomGirlsPostResponseModel:
    owner_room = await database.get_one(OwnerRoomSchema, owner_id)

    owner_room.main_girl_mid = request.main_girl_mid
    owner_room.sub_girl_mid = request.sub_girl_mid

    await database.flush()

    return RoomGirlsPostResponseModel(owner_room=owner_room)
