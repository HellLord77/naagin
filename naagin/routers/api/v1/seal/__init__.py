from fastapi import APIRouter

from naagin.models.api import SealGetResponseModel
from naagin.schemas import ItemSealSchema
from naagin.types.dependencies import DatabaseDependency
from naagin.types.dependencies import OwnerIdDependency

from . import base

router = APIRouter(prefix="/seal")

router.include_router(base.router)


@router.get("")
async def get(database: DatabaseDependency, owner_id: OwnerIdDependency) -> SealGetResponseModel:
    item_seal_list = await database.find_all(ItemSealSchema, ItemSealSchema.owner_id == owner_id)
    return SealGetResponseModel(item_seal_list=item_seal_list)
