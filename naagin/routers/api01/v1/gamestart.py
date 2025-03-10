from fastapi import APIRouter

from naagin.models.api01 import GamestartGetResponseModel

router = APIRouter(prefix="/gamestart")


@router.get("")
async def get() -> GamestartGetResponseModel:
    return GamestartGetResponseModel(gamestart=True)
