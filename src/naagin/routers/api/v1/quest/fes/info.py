from fastapi import APIRouter

from naagin.models.api import QuestFesInfoGetResponseModel

router = APIRouter(prefix="/info")


@router.get("")
async def get() -> QuestFesInfoGetResponseModel:
    return QuestFesInfoGetResponseModel(open_bonus_fes_list=[], quest_daily_info_list=[])
