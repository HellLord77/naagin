from fastapi import APIRouter

from . import bgm

router = APIRouter(prefix="/radio_station")

router.include_router(bgm.router)
