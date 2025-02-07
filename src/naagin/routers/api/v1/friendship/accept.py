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
    request: FriendshipAcceptPostRequestModel, session: SessionDependency, owner_id: OwnerIdDependency
) -> FriendshipAcceptPostResponseModel:
    owner = await session.get_one(OwnerSchema, owner_id)
    owner_other = await session.get_one(OwnerSchema, request.friend_id)
    friendship = await session.get_one(FriendshipSchema, owner_id)
    friendship_other = await session.get_one(FriendshipSchema, request.friend_id)

    if friendship.state == FriendshipStateEnum.RECEIVED and friendship_other.state == FriendshipStateEnum.SENT:
        friendship.state = FriendshipStateEnum.ACCEPTED
        friendship.invited = True
        friendship_other.state = FriendshipStateEnum.ACCEPTED
        friendship.invited = True

    await session.flush()
    await session.refresh(friendship)
    await session.refresh(friendship_other)

    return FriendshipAcceptPostResponseModel(
        friendship_list=[friendship, friendship_other], owner_list=[owner, owner_other]
    )
