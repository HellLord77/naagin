from fastapi import APIRouter

from naagin.models.api import CasinoRouletteLogGetResponseModel

router = APIRouter(prefix="/log")


@router.get("")
async def get() -> CasinoRouletteLogGetResponseModel:
    return CasinoRouletteLogGetResponseModel(roulette_log_list=[])
