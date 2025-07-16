from fastapi import APIRouter

from naagin.enums import FriendshipStateEnum
from naagin.models.api import FriendshipAcceptPostRequestModel
from naagin.models.api import FriendshipAcceptPostResponseModel
from naagin.schemas import FriendshipSchema
from naagin.schemas import OwnerSchema
from naagin.types_.dependencies import DatabaseDependency
from naagin.types_.dependencies import OwnerIdDependency

router = APIRouter(prefix="/accept")


@router.post("")
async def post(
    request: FriendshipAcceptPostRequestModel, database: DatabaseDependency, owner_id: OwnerIdDependency
) -> FriendshipAcceptPostResponseModel:
    owner = await database.get_one(OwnerSchema, owner_id)
    owner_other = await database.get_one(OwnerSchema, request.friend_id)
    friendship = await database.get_one(FriendshipSchema, owner_id)
    friendship_other = await database.get_one(FriendshipSchema, request.friend_id)

    if friendship.state == FriendshipStateEnum.RECEIVED and friendship_other.state == FriendshipStateEnum.SENT:
        friendship.state = FriendshipStateEnum.ACCEPTED
        friendship.invited = True
        friendship_other.state = FriendshipStateEnum.ACCEPTED
        friendship.invited = True

    await database.flush()
    await database.refresh(friendship)
    await database.refresh(friendship_other)

    return FriendshipAcceptPostResponseModel(
        friendship_list=[friendship, friendship_other], owner_list=[owner, owner_other]
    )
