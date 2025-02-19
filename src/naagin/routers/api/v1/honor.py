from fastapi import APIRouter

from naagin.models.api import HonorGetResponseModel
from naagin.schemas import HonorSchema
from naagin.types.dependencies import DatabaseDependency
from naagin.types.dependencies import OwnerIdDependency

router = APIRouter(prefix="/honor")


@router.get("")
async def get(database: DatabaseDependency, owner_id: OwnerIdDependency) -> HonorGetResponseModel:
    honor_list = await database.find_all(HonorSchema, HonorSchema.owner_id == owner_id)
    return HonorGetResponseModel(honor_list=honor_list)
