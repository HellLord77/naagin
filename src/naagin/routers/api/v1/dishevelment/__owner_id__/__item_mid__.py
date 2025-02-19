from fastapi import APIRouter

from naagin.models.api import DishevelmentOwnerIdItemMidGetResponseModel
from naagin.models.api.v1.dishevelment.__owner_id__.__item_mid__.get.response import DishevelmentOtherModel
from naagin.schemas import DishevelmentSwimsuitSchema
from naagin.types.dependencies import SessionDependency

router = APIRouter(prefix="/{item_mid}")


@router.get("")
async def get(owner_id: int, item_mid: int, session: SessionDependency) -> DishevelmentOwnerIdItemMidGetResponseModel:
    dishevelment_swimsuit = await session.get(DishevelmentSwimsuitSchema, (owner_id, item_mid))

    if not_dishevelment := dishevelment_swimsuit is None:
        dishevelment_swimsuit = DishevelmentSwimsuitSchema(owner_id=owner_id, item_mid=item_mid)

    dishevelment_other = DishevelmentOtherModel(
        owner_id=dishevelment_swimsuit.owner_id,
        item_mid=dishevelment_swimsuit.item_mid,
        variation=dishevelment_swimsuit.variation,
        dishevelment=not not_dishevelment,
    )
    return DishevelmentOwnerIdItemMidGetResponseModel(dishevelment_other=dishevelment_other)
