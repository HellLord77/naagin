from fastapi import APIRouter

from naagin.models.api import RoomGirlFriendlyGetResponseModel
from naagin.schemas import FriendlyValueSchema
from naagin.types.dependencies import DatabaseDependency
from naagin.types.dependencies import OwnerIdDependency

router = APIRouter(prefix="/friendly")


@router.get("")
async def get(database: DatabaseDependency, owner_id: OwnerIdDependency) -> RoomGirlFriendlyGetResponseModel:
    friendly_value_list = await database.find_all(FriendlyValueSchema, FriendlyValueSchema.owner_id == owner_id)
    return RoomGirlFriendlyGetResponseModel(friendly_value_list=friendly_value_list)
