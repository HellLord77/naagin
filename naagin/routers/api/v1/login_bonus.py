from fastapi import APIRouter

from naagin.models.api import LoginBonusGetResponseModel
from naagin.schemas import LoginBonusSchema
from naagin.types_.dependencies import DatabaseDependency
from naagin.types_.dependencies import OwnerIdDependency

router = APIRouter(prefix="/login_bonus")


@router.get("")
async def get(database: DatabaseDependency, owner_id: OwnerIdDependency) -> LoginBonusGetResponseModel:
    login_bonus_list = await database.find_all(LoginBonusSchema, LoginBonusSchema.owner_id == owner_id)
    return LoginBonusGetResponseModel(login_bonus_list=login_bonus_list)
