from fastapi import APIRouter

from . import accept

router = APIRouter(prefix="/parameter")

router.include_router(accept.router)
