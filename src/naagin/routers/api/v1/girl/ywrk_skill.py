from fastapi import APIRouter

from naagin.models.api import GirlYwrkSkillGetResponseModel

router = APIRouter(prefix="/ywrk_skill")


@router.get("")
async def get() -> GirlYwrkSkillGetResponseModel:
    raise NotImplementedError
