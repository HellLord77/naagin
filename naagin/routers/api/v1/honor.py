from fastapi import APIRouter
from sqlalchemy import func

from naagin.models.api import HonorGetResponseModel
from naagin.models.api import HonorPostResponseModel
from naagin.schemas import HonorSchema
from naagin.schemas import OwnerCheckedAtSchema
from naagin.types.dependencies import DatabaseDependency
from naagin.types.dependencies import OwnerIdDependency

router = APIRouter(prefix="/honor")


@router.get("")
async def get(database: DatabaseDependency, owner_id: OwnerIdDependency) -> HonorGetResponseModel:
    honor_list = await database.find_all(HonorSchema, HonorSchema.owner_id == owner_id)
    return HonorGetResponseModel(honor_list=honor_list)


@router.post("")
async def post(database: DatabaseDependency, owner_id: OwnerIdDependency) -> HonorPostResponseModel:
    honor_list = await database.find_all(HonorSchema, HonorSchema.owner_id == owner_id)
    owner_checked_at = await database.get_one(OwnerCheckedAtSchema, owner_id)

    owner_checked_at.honor_checked_at = func.current_timestamp()

    await database.flush()
    await database.refresh(owner_checked_at)

    return HonorPostResponseModel(honor_list=honor_list, owner_checked_at_list=[owner_checked_at])
