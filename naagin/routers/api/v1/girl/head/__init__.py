from fastapi import APIRouter

from . import accessory

router = APIRouter(prefix="/head")

router.include_router(accessory.router)
