from fastapi import APIRouter

from naagin.models.api import GirlYwrkSkillGetResponseModel
from naagin.schemas import YwrkSkillSchema
from naagin.types_.dependencies import DatabaseDependency
from naagin.types_.dependencies import OwnerIdDependency

router = APIRouter(prefix="/ywrk_skill")


@router.get("")
async def get(database: DatabaseDependency, owner_id: OwnerIdDependency) -> GirlYwrkSkillGetResponseModel:
    ywrk_skill_list = await database.find_all(YwrkSkillSchema, YwrkSkillSchema.owner_id == owner_id)
    return GirlYwrkSkillGetResponseModel(ywrk_skill_list=ywrk_skill_list)
