from fastapi import APIRouter

from . import __type__

router = APIRouter(prefix="/favorite")

router.include_router(__type__.router)
