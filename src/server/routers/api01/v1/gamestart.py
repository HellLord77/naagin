from fastapi import APIRouter

from ....models.api01.v1.gamestart import GamestartResponseModel

router = APIRouter(prefix="/gamestart")


@router.get("")
async def get() -> GamestartResponseModel:
    return GamestartResponseModel(gamestart=True)
