from fastapi import APIRouter

from naagin.models.api import BromideGetResponseModel
from naagin.schemas import BromideSchema
from naagin.types.dependencies import DatabaseDependency
from naagin.types.dependencies import OwnerIdDependency

router = APIRouter(prefix="/bromide")


@router.get("")
async def get(database: DatabaseDependency, owner_id: OwnerIdDependency) -> BromideGetResponseModel:
    bromide_list = await database.find_all(BromideSchema, BromideSchema.owner_id == owner_id)
    return BromideGetResponseModel(bromide_list=bromide_list)
