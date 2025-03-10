from fastapi import APIRouter

from naagin.models.api import OwnerCountLoginGetResponseModel
from naagin.schemas import OwnerCountLoginSchema
from naagin.types.dependencies import DatabaseDependency
from naagin.types.dependencies import OwnerIdDependency

router = APIRouter(prefix="/countlogin")


@router.get("")
async def get(database: DatabaseDependency, owner_id: OwnerIdDependency) -> OwnerCountLoginGetResponseModel:
    owner_count_login = await database.get_one(OwnerCountLoginSchema, owner_id)
    return OwnerCountLoginGetResponseModel(login_count=owner_count_login.value)
