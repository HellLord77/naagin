from fastapi import APIRouter
from sqlalchemy import select

from naagin.models.api import DishevelmentOwnerIdItemMidGetResponseModel
from naagin.models.api.v1.dishevelment.__owner_id__.__item_mid__.get.response import DishevelmentOtherModel
from naagin.schemas import DishevelmentSchema
from naagin.types.dependencies import SessionDependency

router = APIRouter(prefix="/{item_mid}")


@router.get("")
async def get(owner_id: int, item_mid: int, session: SessionDependency) -> DishevelmentOwnerIdItemMidGetResponseModel:
    dishevelment = await session.scalar(
        select(DishevelmentSchema).where(
            DishevelmentSchema.owner_id == owner_id, DishevelmentSchema.item_mid == item_mid
        )
    )

    variation = 1
    dishevelment_ = dishevelment is not None

    dishevelment_other = DishevelmentOtherModel(
        owner_id=owner_id, item_mid=item_mid, variation=variation, dishevelment=dishevelment_
    )
    return DishevelmentOwnerIdItemMidGetResponseModel(dishevelment_other=dishevelment_other)
