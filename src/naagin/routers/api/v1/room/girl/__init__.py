from fastapi import APIRouter

from . import friendly

router = APIRouter(prefix="/girl")

router.include_router(friendly.router)
