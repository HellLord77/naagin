from fastapi import APIRouter
from sqlalchemy import select

from naagin.models.api import FriendshipReceivedGetResponseModel
from naagin.schemas import FriendshipSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency
from naagin.types.enums import FriendshipStateEnum

router = APIRouter(prefix="/received")


@router.get("")
async def get(
    session: SessionDependency, owner_id: OwnerIdDependency
) -> FriendshipReceivedGetResponseModel:
    friendships = (
        await session.scalars(
            select(FriendshipSchema).where(
                FriendshipSchema.owner_id == owner_id,
                FriendshipSchema.state == FriendshipStateEnum.RECEIVED,
            )
        )
    ).all()
    return FriendshipReceivedGetResponseModel(friendship_list=friendships)
