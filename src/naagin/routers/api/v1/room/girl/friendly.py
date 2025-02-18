from fastapi import APIRouter

from naagin.models.api import RoomGirlFriendlyGetResponseModel
from naagin.schemas import FriendlyValueSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency

router = APIRouter(prefix="/friendly")


@router.get("")
async def get(session: SessionDependency, owner_id: OwnerIdDependency) -> RoomGirlFriendlyGetResponseModel:
    friendly_value_list = await session.find_all(FriendlyValueSchema, FriendlyValueSchema.owner_id == owner_id)
    return RoomGirlFriendlyGetResponseModel(friendly_value_list=friendly_value_list)
