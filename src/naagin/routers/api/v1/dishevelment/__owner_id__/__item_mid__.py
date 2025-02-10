from fastapi import APIRouter

from naagin.models.api import DishevelmentOwnerIdItemMidGetResponseModel
from naagin.schemas import DishevelmentSwimsuitSchema
from naagin.types.dependencies import SessionDependency

router = APIRouter(prefix="/{item_mid}")


@router.get("")
async def get(owner_id: int, item_mid: int, session: SessionDependency) -> DishevelmentOwnerIdItemMidGetResponseModel:
    dishevelment_other = await session.find(
        DishevelmentSwimsuitSchema,
        DishevelmentSwimsuitSchema.owner_id == owner_id,
        DishevelmentSwimsuitSchema.item_mid == item_mid,
    )

    dishevelment = dishevelment_other is not None
    if not dishevelment:
        dishevelment_other = DishevelmentSwimsuitSchema(owner_id=owner_id, item_mid=item_mid)
    dishevelment_other.dishevelment = dishevelment

    return DishevelmentOwnerIdItemMidGetResponseModel(dishevelment_other=dishevelment_other)
