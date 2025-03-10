from fastapi import APIRouter

from . import panel
from . import status

router = APIRouter(prefix="/venus_board")

router.include_router(panel.router)
router.include_router(status.router)
