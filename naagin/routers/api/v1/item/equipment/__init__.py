from fastapi import APIRouter

from . import type

router = APIRouter(prefix="/equipment")

router.include_router(type.router)
