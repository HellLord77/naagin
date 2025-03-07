from fastapi import APIRouter

from . import list

router = APIRouter(prefix="/guest")

router.include_router(list.router)
