from fastapi import APIRouter
from sqlalchemy import select

from naagin.enums import FriendshipStateEnum
from naagin.exceptions import FriendshipCantRequestException
from naagin.models.api import FriendshipGetResponseModel
from naagin.models.api import FriendshipPostRequestModel
from naagin.models.api import FriendshipPostResponseModel
from naagin.schemas import FriendshipSchema
from naagin.schemas import OwnerSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency

from . import __other_owner_id__
from . import accept
from . import received
from . import sent

router = APIRouter(prefix="/friendship")

router.include_router(__other_owner_id__.router)
router.include_router(accept.router)
router.include_router(received.router)
router.include_router(sent.router)


@router.get("")
async def get(
    session: SessionDependency, owner_id: OwnerIdDependency
) -> FriendshipGetResponseModel:
    friendship_list = (
        await session.scalars(
            select(FriendshipSchema).where(
                FriendshipSchema.owner_id == owner_id,
                FriendshipSchema.state == FriendshipStateEnum.ACCEPTED,
                FriendshipSchema.invited,
            )
        )
    ).all()
    return FriendshipGetResponseModel(friendship_list=friendship_list)


@router.post("")
async def post(
    request: FriendshipPostRequestModel,
    session: SessionDependency,
    owner_id: OwnerIdDependency,
) -> FriendshipPostResponseModel:
    owner = await session.get_one(OwnerSchema, owner_id)
    other_owner = await session.get_one(OwnerSchema, request.friend_id)
    friendship = await session.get(FriendshipSchema, owner_id, request.friend_id)
    other_friendship = await session.get(FriendshipSchema, request.friend_id, owner_id)

    if friendship is None and other_friendship is None:
        friendship = FriendshipSchema(
            owner_id=owner_id,
            friend_id=request.friend_id,
            state=FriendshipStateEnum.SENT,
        )
        other_friendship = FriendshipSchema(
            owner_id=request.friend_id,
            friend_id=owner_id,
            state=FriendshipStateEnum.RECEIVED,
        )
        session.add(friendship)
        session.add(other_friendship)
    elif other_friendship.state == FriendshipStateEnum.BLOCKED:
        raise FriendshipCantRequestException
    elif (
        (
            friendship.state == FriendshipStateEnum.BLOCKED
            and other_friendship.state == FriendshipStateEnum.REJECTED
        )
        or (
            friendship.state == FriendshipStateEnum.RETRACTED
            and other_friendship.state == FriendshipStateEnum.RETRACTED
        )
        or (
            friendship.state == FriendshipStateEnum.UNINVITED
            and other_friendship.state == FriendshipStateEnum.UNINVITED
        )
    ):
        friendship.state = FriendshipStateEnum.SENT
        other_friendship.state = FriendshipStateEnum.RECEIVED

    await session.flush()
    await session.refresh(friendship)
    await session.refresh(other_friendship)
    return FriendshipPostResponseModel(
        friendship_list=[friendship, other_friendship], owner_list=[owner, other_owner]
    )
