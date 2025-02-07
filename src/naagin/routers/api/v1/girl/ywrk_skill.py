from fastapi import APIRouter

from naagin.models.api import GirlYwrkSkillGetResponseModel
from naagin.schemas import YwrkSkillSchema
from naagin.types.dependencies import OwnerIdDependency
from naagin.types.dependencies import SessionDependency

router = APIRouter(prefix="/ywrk_skill")


@router.get("")
async def get(session: SessionDependency, owner_id: OwnerIdDependency) -> GirlYwrkSkillGetResponseModel:
    ywrk_skill_list = await session.get_all(YwrkSkillSchema, YwrkSkillSchema.owner_id == owner_id)
    return GirlYwrkSkillGetResponseModel(ywrk_skill_list=ywrk_skill_list)
