from fastapi import APIRouter

from naagin.models.api import SealBaseGetResponseModel
from naagin.schemas import SealBaseSchema
from naagin.types.dependencies import DatabaseDependency
from naagin.types.dependencies import OwnerIdDependency

router = APIRouter(prefix="/base")


@router.get("")
async def get(database: DatabaseDependency, owner_id: OwnerIdDependency) -> SealBaseGetResponseModel:
    seal_base_list = await database.find_all(SealBaseSchema, SealBaseSchema.owner_id == owner_id)
    return SealBaseGetResponseModel(seal_base_list=seal_base_list)
