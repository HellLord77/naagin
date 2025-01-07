from fastapi import APIRouter

from ....models.api01.v1.gamestart import GamestartGetResponseModel

router = APIRouter(prefix="/gamestart")


@router.get("")
async def get() -> GamestartGetResponseModel:
    return GamestartGetResponseModel(gamestart=True)
