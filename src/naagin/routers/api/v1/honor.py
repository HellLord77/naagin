from fastapi import APIRouter

from naagin.models.api import HonorGetResponseModel
from naagin.schemas import HonorSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency

router = APIRouter(prefix="/honor")


@router.get("")
async def get(session: SessionDependency, owner_id: OwnerIdDependency) -> HonorGetResponseModel:
    honor_list = await session.get_all(HonorSchema, HonorSchema.owner_id == owner_id)
    return HonorGetResponseModel(honor_list=honor_list)
