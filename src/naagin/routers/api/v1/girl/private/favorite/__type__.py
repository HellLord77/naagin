from fastapi import APIRouter
from sqlalchemy import select

from naagin.enums import PrivateItemTypeEnum
from naagin.exceptions import InternalServerErrorException
from naagin.models.api import GirlPrivateFavoriteTypeGetResponseModel
from naagin.schemas import PrivateItemSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency

router = APIRouter(prefix="/{type}")


@router.get("")
async def get(
    type: PrivateItemTypeEnum,
    session: SessionDependency,
    owner_id: OwnerIdDependency,
) -> GirlPrivateFavoriteTypeGetResponseModel:
    if type == PrivateItemTypeEnum._VALUE_80:
        raise InternalServerErrorException

    favorite_private_item_list = (
        await session.scalars(
            select(PrivateItemSchema).where(
                PrivateItemSchema.owner_id == owner_id, PrivateItemSchema.type == type
            )
        )
    ).all()
    return GirlPrivateFavoriteTypeGetResponseModel(
        favorite_private_item_list=favorite_private_item_list
    )
