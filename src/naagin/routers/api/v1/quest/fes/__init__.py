from fastapi import APIRouter

from . import info

router = APIRouter(prefix="/fes")

router.include_router(info.router)
