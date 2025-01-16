from fastapi import APIRouter

from . import item_auto_lock

router = APIRouter(prefix="/option")

router.include_router(item_auto_lock.router)
