from fastapi import APIRouter

from . import __type__

router = APIRouter(prefix="/special_order")

router.include_router(__type__.router)
