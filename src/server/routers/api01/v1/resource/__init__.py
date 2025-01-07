from fastapi import APIRouter

from . import list

router = APIRouter(prefix="/resource")

router.include_router(list.router)
