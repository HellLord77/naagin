from fastapi import APIRouter

from . import favorite

router = APIRouter(prefix="/private")

router.include_router(favorite.router)
