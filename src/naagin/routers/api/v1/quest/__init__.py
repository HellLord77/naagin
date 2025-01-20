from fastapi import APIRouter

from . import check

router = APIRouter(prefix="/quest")

router.include_router(check.router)
