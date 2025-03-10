from fastapi import APIRouter

from . import switch

router = APIRouter(prefix="/accessory")

router.include_router(switch.router)
