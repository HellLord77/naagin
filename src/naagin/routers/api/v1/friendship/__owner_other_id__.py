from fastapi import APIRouter

from naagin.enums import FriendshipStateEnum
from naagin.models.api import FriendshipFriendIdDeleteResponseModel
from naagin.schemas import FriendshipSchema
from naagin.schemas import OwnerSchema
from naagin.types.dependencies import DatabaseDependency
from naagin.types.dependencies import OwnerIdDependency

router = APIRouter(prefix="/{owner_other_id}")


@router.delete("")
async def delete(
    owner_other_id: int, database: DatabaseDependency, owner_id: OwnerIdDependency
) -> FriendshipFriendIdDeleteResponseModel:
    owner = await database.get_one(OwnerSchema, owner_id)
    owner_other = await database.get_one(OwnerSchema, owner_other_id)
    friendship = await database.get_one(FriendshipSchema, (owner_id, owner_other_id))
    friendship_other = await database.get_one(FriendshipSchema, (owner_other_id, owner_id))

    success = True
    owner_list = None
    if friendship.state == FriendshipStateEnum.SENT and friendship_other.state == FriendshipStateEnum.RECEIVED:
        friendship.state = FriendshipStateEnum.RETRACTED
        friendship_other.state = FriendshipStateEnum.RETRACTED
    elif friendship.state == FriendshipStateEnum.RECEIVED and friendship_other.state == FriendshipStateEnum.SENT:
        friendship.state = FriendshipStateEnum.BLOCKED
        friendship_other.state = FriendshipStateEnum.REJECTED
    elif friendship.state == FriendshipStateEnum.ACCEPTED and friendship_other.state == FriendshipStateEnum.ACCEPTED:
        friendship.state = FriendshipStateEnum.UNINVITED
        friendship_other.state = FriendshipStateEnum.UNINVITED
        owner_list = [owner, owner_other]
    else:
        success = False

    if success:
        await database.flush()
        await database.refresh(friendship)
        await database.refresh(friendship_other)

    return FriendshipFriendIdDeleteResponseModel(friendship_list=[friendship, friendship_other], owner_list=owner_list)
