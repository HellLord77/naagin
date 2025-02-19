from fastapi import APIRouter

from naagin.models.api import MaxCombineOwnerIdItemMidGetResponseModel
from naagin.models.api.v1.max_combine.__owner_id__.__item_mid__.get.response import MaxCombineOtherModel
from naagin.schemas import MaxCombineSwimsuitSchema
from naagin.types.dependencies import DatabaseDependency

router = APIRouter(prefix="/{item_mid}")


@router.get("")
async def get(owner_id: int, item_mid: int, database: DatabaseDependency) -> MaxCombineOwnerIdItemMidGetResponseModel:
    max_combine_swimsuit = await database.get(MaxCombineSwimsuitSchema, (owner_id, item_mid))

    if not_max_combine := max_combine_swimsuit is None:
        max_combine_swimsuit = MaxCombineSwimsuitSchema(owner_id=owner_id, item_mid=item_mid)

    max_combine_other = MaxCombineOtherModel(
        owner_id=max_combine_swimsuit.owner_id,
        item_mid=max_combine_swimsuit.item_mid,
        variation=max_combine_swimsuit.variation,
        max_combine=not not_max_combine,
    )
    return MaxCombineOwnerIdItemMidGetResponseModel(max_combine_other=max_combine_other)
