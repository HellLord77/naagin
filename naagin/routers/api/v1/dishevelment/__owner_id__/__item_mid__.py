from fastapi import APIRouter

from naagin.models.api import DishevelmentOwnerIdItemMidGetResponseModel
from naagin.models.api.v1.dishevelment.__owner_id__.__item_mid__.get.response import DishevelmentOtherModel
from naagin.schemas import DishevelmentSwimsuitSchema
from naagin.types_.dependencies import DatabaseDependency

router = APIRouter(prefix="/{item_mid}")


@router.get("")
async def get(owner_id: int, item_mid: int, database: DatabaseDependency) -> DishevelmentOwnerIdItemMidGetResponseModel:
    dishevelment_swimsuit = await database.get(DishevelmentSwimsuitSchema, (owner_id, item_mid))

    dishevelment = dishevelment_swimsuit is not None
    if not dishevelment:
        dishevelment_swimsuit = DishevelmentSwimsuitSchema(owner_id=owner_id, item_mid=item_mid)

    dishevelment_other = DishevelmentOtherModel(
        owner_id=dishevelment_swimsuit.owner_id,
        item_mid=dishevelment_swimsuit.item_mid,
        variation=dishevelment_swimsuit.variation,
        dishevelment=dishevelment,
    )
    return DishevelmentOwnerIdItemMidGetResponseModel(dishevelment_other=dishevelment_other)
