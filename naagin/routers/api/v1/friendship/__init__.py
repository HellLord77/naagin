from fastapi import APIRouter

from naagin.enums import FriendshipStateEnum
from naagin.exceptions import FriendshipCantRequestException
from naagin.models.api import FriendshipGetResponseModel
from naagin.models.api import FriendshipPostRequestModel
from naagin.models.api import FriendshipPostResponseModel
from naagin.schemas import FriendshipSchema
from naagin.schemas import OwnerSchema
from naagin.types_.dependencies import DatabaseDependency
from naagin.types_.dependencies import OwnerIdDependency

from . import __owner_other_id__
from . import accept
from . import received
from . import sent

router = APIRouter(prefix="/friendship")

router.include_router(__owner_other_id__.router)
router.include_router(accept.router)
router.include_router(received.router)
router.include_router(sent.router)


@router.get("")
async def get(database: DatabaseDependency, owner_id: OwnerIdDependency) -> FriendshipGetResponseModel:
    friendship_list = await database.find_all(
        FriendshipSchema, FriendshipSchema.owner_id == owner_id, FriendshipSchema.state == FriendshipStateEnum.ACCEPTED
    )
    return FriendshipGetResponseModel(friendship_list=friendship_list)


@router.post("")
async def post(
    request: FriendshipPostRequestModel, database: DatabaseDependency, owner_id: OwnerIdDependency
) -> FriendshipPostResponseModel:
    owner = await database.get_one(OwnerSchema, owner_id)
    owner_other = await database.get_one(OwnerSchema, request.friend_id)
    friendship = await database.get(FriendshipSchema, (owner_id, request.friend_id))
    friendship_other = await database.get(FriendshipSchema, (request.friend_id, owner_id))

    success = True
    if friendship is None and friendship_other is None:
        friendship = FriendshipSchema(owner_id=owner_id, friend_id=request.friend_id, state=FriendshipStateEnum.SENT)
        friendship_other = FriendshipSchema(
            owner_id=request.friend_id, friend_id=owner_id, state=FriendshipStateEnum.RECEIVED
        )
        database.add(friendship)
        database.add(friendship_other)
    elif friendship_other.state == FriendshipStateEnum.BLOCKED:
        raise FriendshipCantRequestException
    elif (
        (friendship.state == FriendshipStateEnum.BLOCKED and friendship_other.state == FriendshipStateEnum.REJECTED)
        or (
            friendship.state == FriendshipStateEnum.RETRACTED
            and friendship_other.state == FriendshipStateEnum.RETRACTED
        )
        or (
            friendship.state == FriendshipStateEnum.UNINVITED
            and friendship_other.state == FriendshipStateEnum.UNINVITED
        )
    ):
        friendship.state = FriendshipStateEnum.SENT
        friendship_other.state = FriendshipStateEnum.RECEIVED
    else:
        success = False

    if success:
        await database.flush()
        await database.refresh(friendship)
        await database.refresh(friendship_other)

    return FriendshipPostResponseModel(friendship_list=[friendship, friendship_other], owner_list=[owner, owner_other])
