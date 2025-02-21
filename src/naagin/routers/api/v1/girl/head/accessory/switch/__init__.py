from fastapi import APIRouter

from . import list

router = APIRouter(prefix="/switch")

router.include_router(list.router)
