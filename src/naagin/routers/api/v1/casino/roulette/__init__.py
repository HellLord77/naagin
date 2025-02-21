from fastapi import APIRouter

from naagin.models.api import CasinoRouletteGetResponseModel

from . import log

router = APIRouter(prefix="/roulette")

router.include_router(log.router)


@router.get("")
async def get() -> CasinoRouletteGetResponseModel:
    return CasinoRouletteGetResponseModel(roulette_info_list=[])
