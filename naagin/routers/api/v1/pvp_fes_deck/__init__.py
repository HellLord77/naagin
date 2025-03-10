from fastapi import APIRouter

from . import equipment_list_all

router = APIRouter(prefix="/pvp_fes_deck")

router.include_router(equipment_list_all.router)
