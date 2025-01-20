from fastapi import APIRouter

from . import equipment

router = APIRouter(prefix="/item")

router.include_router(equipment.router)
