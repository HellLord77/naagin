from fastapi import APIRouter

from naagin.models.api import QuestStaminaGetResponseModel

router = APIRouter(prefix="/stamina")


@router.get("")
async def get() -> QuestStaminaGetResponseModel:
    return QuestStaminaGetResponseModel(quest_girl_stamina_list=[])
