from fastapi import APIRouter
from sqlalchemy import select

from naagin.models.api import FriendshipGetResponseModel
from naagin.schemas import FriendshipSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency
from naagin.types.enums import FriendshipStateEnum
from . import received
from . import sent

router = APIRouter(prefix="/friendship")

router.include_router(received.router)
router.include_router(sent.router)


@router.get("")
async def get(
    session: SessionDependency, owner_id: OwnerIdDependency
) -> FriendshipGetResponseModel:
    friendships = (
        await session.scalars(
            select(FriendshipSchema).where(
                FriendshipSchema.owner_id == owner_id,
                FriendshipSchema.state == FriendshipStateEnum.ACCEPTED,
                FriendshipSchema.invited,
            )
        )
    ).all()
    return FriendshipGetResponseModel(friendship_list=friendships)
