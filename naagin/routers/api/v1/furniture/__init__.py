from fastapi import APIRouter

from naagin.models.api import FurnitureGetResponseModel
from naagin.schemas import ItemFurnitureSchema
from naagin.types_.dependencies import DatabaseDependency
from naagin.types_.dependencies import OwnerIdDependency

from . import myset

router = APIRouter(prefix="/furniture")

router.include_router(myset.router)


@router.get("")
async def get(database: DatabaseDependency, owner_id: OwnerIdDependency) -> FurnitureGetResponseModel:
    item_furniture_list = await database.find_all(ItemFurnitureSchema, ItemFurnitureSchema.owner_id == owner_id)
    return FurnitureGetResponseModel(item_furniture_list=item_furniture_list)
