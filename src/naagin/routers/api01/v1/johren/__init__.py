from fastapi import APIRouter

from . import authJohren

router = APIRouter(prefix="/johren")

router.include_router(authJohren.router)
