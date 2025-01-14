from fastapi import APIRouter

from . import check

router = APIRouter(prefix="/cheat_log")

router.include_router(check.router)
