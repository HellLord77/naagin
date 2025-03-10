from fastapi import APIRouter

from . import __onetime_token__

router = APIRouter(prefix="/authJohren")

router.include_router(__onetime_token__.router)
