from fastapi import APIRouter

from . import consume
from . import equipment

router = APIRouter(prefix="/item")

router.include_router(consume.router)
router.include_router(equipment.router)
