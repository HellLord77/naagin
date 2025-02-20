from fastapi import APIRouter

from . import list

router = APIRouter(prefix="/request")

router.include_router(list.router)
