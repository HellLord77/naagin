from fastapi import APIRouter

from naagin.models.api import MaxCombineGetResponseModel
from naagin.schemas import MaxCombineSwimsuitSchema
from naagin.types_.dependencies import DatabaseDependency
from naagin.types_.dependencies import OwnerIdDependency

from . import __owner_id__

router = APIRouter(prefix="/max_combine")

router.include_router(__owner_id__.router)


@router.get("")
async def get(database: DatabaseDependency, owner_id: OwnerIdDependency) -> MaxCombineGetResponseModel:
    max_combine_swimsuit_list = await database.find_all(
        MaxCombineSwimsuitSchema, MaxCombineSwimsuitSchema.owner_id == owner_id
    )
    return MaxCombineGetResponseModel(max_combine_swimsuit_list=max_combine_swimsuit_list)
