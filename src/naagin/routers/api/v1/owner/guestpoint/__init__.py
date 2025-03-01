from fastapi import APIRouter

from . import accept

router = APIRouter(prefix="/guestpoint")

router.include_router(accept.router)
