from fastapi import APIRouter

from . import list

router = APIRouter(prefix="/csv")

router.include_router(list.router)
