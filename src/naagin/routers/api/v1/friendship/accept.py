from fastapi import APIRouter

from naagin.enums import FriendshipStateEnum
from naagin.models.api import FriendshipAcceptPostRequestModel
from naagin.models.api import FriendshipAcceptPostResponseModel
from naagin.schemas import FriendshipSchema
from naagin.schemas import OwnerSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency

router = APIRouter(prefix="/accept")


@router.post("")
async def post(
    request: FriendshipAcceptPostRequestModel,
    session: SessionDependency,
    owner_id: OwnerIdDependency,
) -> FriendshipAcceptPostResponseModel:
    owner = await session.get_one(OwnerSchema, owner_id)
    other_owner = await session.get_one(OwnerSchema, request.friend_id)
    friendship = await session.get_one(FriendshipSchema, owner_id)
    other_friendship = await session.get_one(FriendshipSchema, request.friend_id)

    if (
        friendship.state == FriendshipStateEnum.RECEIVED
        and other_friendship.state == FriendshipStateEnum.SENT
    ):
        friendship.state = FriendshipStateEnum.ACCEPTED
        friendship.invited = True
        other_friendship.state = FriendshipStateEnum.ACCEPTED
        friendship.invited = True

    await session.flush()
    await session.refresh(friendship)
    await session.refresh(other_friendship)
    return FriendshipAcceptPostResponseModel(
        friendship_list=[friendship, other_friendship], owner_list=[owner, other_owner]
    )
