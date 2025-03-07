from fastapi import APIRouter

from . import shoot
from . import today_count

router = APIRouter(prefix="/photo_shoot")

router.include_router(shoot.router)
router.include_router(today_count.router)
