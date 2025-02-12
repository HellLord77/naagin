from fastapi import APIRouter

from naagin.models.api import FurnitureMySetOwnerIdListGetResponseModel
from naagin.schemas import FurnitureMySetSchema
from naagin.types.dependencies import SessionDependency

router = APIRouter(prefix="/list")


@router.get("")
async def get(owner_id: int, session: SessionDependency) -> FurnitureMySetOwnerIdListGetResponseModel:
    other_furniture_myset_list = await session.find_all(FurnitureMySetSchema, FurnitureMySetSchema.owner_id == owner_id)
    return FurnitureMySetOwnerIdListGetResponseModel(other_furniture_myset_list=other_furniture_myset_list)
