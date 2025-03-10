from fastapi import APIRouter

from . import list

router = APIRouter(prefix="/{owner_id}")

router.include_router(list.router)
