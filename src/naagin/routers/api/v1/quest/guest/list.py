from fastapi import APIRouter

from naagin.models.api import QuestGuestListGetResponseModel

router = APIRouter(prefix="/list")


@router.get("")
async def get() -> QuestGuestListGetResponseModel:
    return QuestGuestListGetResponseModel(guest_list=[])
