from fastapi import APIRouter

from . import license_point

router = APIRouter(prefix="/check")

router.include_router(license_point.router)
