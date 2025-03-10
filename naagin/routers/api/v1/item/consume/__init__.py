from fastapi import APIRouter

from naagin.models.api import ItemConsumeGetResponseModel
from naagin.schemas import ItemConsumeSchema
from naagin.types.dependencies import DatabaseDependency
from naagin.types.dependencies import OwnerIdDependency

from . import negative

router = APIRouter(prefix="/consume")

router.include_router(negative.router)


@router.get("")
async def get(database: DatabaseDependency, owner_id: OwnerIdDependency) -> ItemConsumeGetResponseModel:
    item_consume_list = await database.find_all(ItemConsumeSchema, ItemConsumeSchema.owner_id == owner_id)
    return ItemConsumeGetResponseModel(item_consume_list=item_consume_list)
