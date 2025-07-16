from fastapi import APIRouter

from naagin.enums import FriendshipStateEnum
from naagin.models.api import FriendshipSentGetResponseModel
from naagin.schemas import FriendshipSchema
from naagin.types_.dependencies import DatabaseDependency
from naagin.types_.dependencies import OwnerIdDependency

router = APIRouter(prefix="/sent")


@router.get("")
async def get(database: DatabaseDependency, owner_id: OwnerIdDependency) -> FriendshipSentGetResponseModel:
    friendship_list = await database.find_all(
        FriendshipSchema, FriendshipSchema.owner_id == owner_id, FriendshipSchema.state == FriendshipStateEnum.SENT
    )
    return FriendshipSentGetResponseModel(friendship_list=friendship_list)
