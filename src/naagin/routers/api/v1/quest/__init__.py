from fastapi import APIRouter

from . import check
from . import fes
from . import stamina

router = APIRouter(prefix="/quest")

router.include_router(check.router)
router.include_router(fes.router)
router.include_router(stamina.router)
