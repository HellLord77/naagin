from fastapi import APIRouter

from . import check
from . import fes
from . import guest
from . import list
from . import stamina

router = APIRouter(prefix="/quest")

router.include_router(check.router)
router.include_router(fes.router)
router.include_router(guest.router)
router.include_router(list.router)
router.include_router(stamina.router)
