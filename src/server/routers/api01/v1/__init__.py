from fastapi import APIRouter

from . import gamestart
from . import maintenance
from . import resource

router = APIRouter(prefix="/v1")

router.include_router(gamestart.router)
router.include_router(maintenance.router)
router.include_router(resource.router)
