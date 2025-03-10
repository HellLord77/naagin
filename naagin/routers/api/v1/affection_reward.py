from fastapi import APIRouter

from naagin.models.api import AffectionRewardGetResponseModel

router = APIRouter(prefix="/affection_reward")


@router.get("")
async def get() -> AffectionRewardGetResponseModel:
    return AffectionRewardGetResponseModel(affection_level_reward_list=[])
