from fastapi import APIRouter

from naagin.models.api import FurnitureMySetGetResponseModel
from naagin.schemas import FurnitureMySetSchema
from naagin.types.dependencies import DatabaseDependency
from naagin.types.dependencies import OwnerIdDependency

from . import __owner_id__

router = APIRouter(prefix="/myset")

router.include_router(__owner_id__.router)


@router.get("")
async def get(database: DatabaseDependency, owner_id: OwnerIdDependency) -> FurnitureMySetGetResponseModel:
    furniture_myset_list = await database.find_all(FurnitureMySetSchema, FurnitureMySetSchema.owner_id == owner_id)
    return FurnitureMySetGetResponseModel(furniture_myset_list=furniture_myset_list)
