from fastapi import APIRouter

from . import equipment

router = APIRouter(prefix="/pvp_girl")

router.include_router(equipment.router)
