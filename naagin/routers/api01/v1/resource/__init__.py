from fastapi import APIRouter

from . import key
from . import list

router = APIRouter(prefix="/resource")

router.include_router(key.router)
router.include_router(list.router)
