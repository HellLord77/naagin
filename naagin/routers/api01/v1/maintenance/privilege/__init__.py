from fastapi import APIRouter

from . import check

router = APIRouter(prefix="/privilege")

router.include_router(check.router)
