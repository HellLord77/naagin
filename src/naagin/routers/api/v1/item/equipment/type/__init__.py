from fastapi import APIRouter

from . import __type__

router = APIRouter(prefix="/type")

router.include_router(__type__.router)
