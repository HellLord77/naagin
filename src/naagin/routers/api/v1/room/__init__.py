from fastapi import APIRouter

from naagin.models.api import RoomPostResponseModel
from naagin.schemas import OwnerRoomSchema
from naagin.types.dependencies import DatabaseDependency
from naagin.types.dependencies import OwnerIdDependency

from . import girl
from . import girls
from . import request

router = APIRouter(prefix="/room")

router.include_router(girl.router)
router.include_router(girls.router)
router.include_router(request.router)


@router.post("")
async def post(database: DatabaseDependency, owner_id: OwnerIdDependency) -> RoomPostResponseModel:
    owner_room = await database.get(OwnerRoomSchema, owner_id)

    if owner_room is None:
        owner_room = OwnerRoomSchema(owner_id=owner_id)

        database.add(owner_room)
        await database.flush()

    return RoomPostResponseModel(owner_room=owner_room)
