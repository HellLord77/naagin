from fastapi import APIRouter

from naagin.enums import FriendshipStateEnum
from naagin.models.api import FriendshipFriendIdDeleteResponseModel
from naagin.schemas import FriendshipSchema
from naagin.schemas import OwnerSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency

router = APIRouter(prefix="/{other_owner_id}")


@router.delete("")
async def delete(
    other_owner_id: int, session: SessionDependency, owner_id: OwnerIdDependency
) -> FriendshipFriendIdDeleteResponseModel:
    owner = await session.get_one(OwnerSchema, owner_id)
    other_owner = await session.get_one(OwnerSchema, other_owner_id)
    friendship = await session.get_one(FriendshipSchema, owner_id, other_owner_id)
    other_friendship = await session.get_one(FriendshipSchema, other_owner_id, owner_id)

    owner_list = None
    if (
        friendship.state == FriendshipStateEnum.SENT
        and other_friendship.state == FriendshipStateEnum.RECEIVED
    ):
        friendship.state = FriendshipStateEnum.RETRACTED
        other_friendship.state = FriendshipStateEnum.RETRACTED
    elif (
        friendship.state == FriendshipStateEnum.RECEIVED
        and other_friendship.state == FriendshipStateEnum.SENT
    ):
        friendship.state = FriendshipStateEnum.BLOCKED
        other_friendship.state = FriendshipStateEnum.REJECTED
    elif (
        friendship.state == FriendshipStateEnum.ACCEPTED
        and other_friendship.state == FriendshipStateEnum.ACCEPTED
    ):
        friendship.state = FriendshipStateEnum.UNINVITED
        other_friendship.state = FriendshipStateEnum.UNINVITED
        owner_list = [owner, other_owner]

    await session.flush()
    await session.refresh(friendship)
    await session.refresh(other_friendship)
    return FriendshipFriendIdDeleteResponseModel(
        friendship_list=[friendship, other_friendship], owner_list=owner_list
    )
