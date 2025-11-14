from fastapi import APIRouter

from . import __platform_id__

router = APIRouter(prefix="/key")

router.include_router(__platform_id__.router)
