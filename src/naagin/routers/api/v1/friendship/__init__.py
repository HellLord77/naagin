from fastapi import APIRouter

from naagin.enums import FriendshipStateEnum
from naagin.exceptions import FriendshipCantRequestException
from naagin.models.api import FriendshipGetResponseModel
from naagin.models.api import FriendshipPostRequestModel
from naagin.models.api import FriendshipPostResponseModel
from naagin.schemas import FriendshipSchema
from naagin.schemas import OwnerSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency

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
async def get(session: SessionDependency, owner_id: OwnerIdDependency) -> FriendshipGetResponseModel:
    friendship_list = await session.get_all(
        FriendshipSchema, FriendshipSchema.owner_id == owner_id, FriendshipSchema.state == FriendshipStateEnum.ACCEPTED
    )
    return FriendshipGetResponseModel(friendship_list=friendship_list)


@router.post("")
async def post(
    request: FriendshipPostRequestModel, session: SessionDependency, owner_id: OwnerIdDependency
) -> FriendshipPostResponseModel:
    owner = await session.get_one(OwnerSchema, owner_id)
    owner_other = await session.get_one(OwnerSchema, request.friend_id)
    friendship = await session.get(FriendshipSchema, owner_id, request.friend_id)
    friendship_other = await session.get(FriendshipSchema, request.friend_id, owner_id)

    if friendship is None and friendship_other is None:
        friendship = FriendshipSchema(owner_id=owner_id, friend_id=request.friend_id, state=FriendshipStateEnum.SENT)
        friendship_other = FriendshipSchema(
            owner_id=request.friend_id, friend_id=owner_id, state=FriendshipStateEnum.RECEIVED
        )
        session.add(friendship)
        session.add(friendship_other)
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

    await session.flush()
    await session.refresh(friendship)
    await session.refresh(friendship_other)
    return FriendshipPostResponseModel(friendship_list=[friendship, friendship_other], owner_list=[owner, owner_other])
