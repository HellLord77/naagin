from fastapi import APIRouter

from . import girl

router = APIRouter(prefix="/room")

router.include_router(girl.router)
