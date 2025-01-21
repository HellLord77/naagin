from fastapi import APIRouter
from sqlalchemy import select

from naagin.models.api import GirlGirlMidPrivateFavoriteTypeGetResponseModel
from naagin.schemas import PrivateItemSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency
from naagin.types.enums import BooleanEnum
from naagin.types.enums import PrivateItemTypeEnum

router = APIRouter(prefix="/{type}")


@router.get("")
async def get(
    girl_mid: int,
    type: PrivateItemTypeEnum,
    session: SessionDependency,
    owner_id: OwnerIdDependency,
) -> GirlGirlMidPrivateFavoriteTypeGetResponseModel:
    favorite_private_item_list = (
        await session.scalars(
            select(PrivateItemSchema).where(
                PrivateItemSchema.owner_id == owner_id,
                PrivateItemSchema.girl_mid == girl_mid,
                PrivateItemSchema.type == type,
                PrivateItemSchema.favorite == BooleanEnum.TRUE,
            )
        )
    ).all()
    return GirlGirlMidPrivateFavoriteTypeGetResponseModel(
        favorite_private_item_list=favorite_private_item_list
    )
