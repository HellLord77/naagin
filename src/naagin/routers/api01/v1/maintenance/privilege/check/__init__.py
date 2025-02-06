from fastapi import APIRouter

from . import __steam_id__

router = APIRouter(prefix="/check")

router.include_router(__steam_id__.router)
