from fastapi import APIRouter

from naagin.models.api import MaxCombineOwnerIdItemMidGetResponseModel
from naagin.schemas import MaxCombineSwimsuitSchema
from naagin.types.dependencies import SessionDependency

router = APIRouter(prefix="/{item_mid}")


@router.get("")
async def get(owner_id: int, item_mid: int, session: SessionDependency) -> MaxCombineOwnerIdItemMidGetResponseModel:
    max_combine_other = await session.find(
        MaxCombineSwimsuitSchema,
        MaxCombineSwimsuitSchema.owner_id == owner_id,
        MaxCombineSwimsuitSchema.item_mid == item_mid,
    )

    max_combine = max_combine_other is not None
    if not max_combine:
        max_combine_other = MaxCombineSwimsuitSchema(owner_id=owner_id, item_mid=item_mid)
    max_combine_other.max_combine = max_combine

    return MaxCombineOwnerIdItemMidGetResponseModel(max_combine_other=max_combine_other)
