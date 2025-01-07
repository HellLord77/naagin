from fastapi import APIRouter

from . import privilege
from .....models.api01.v1.maintenance import MaintenanceResponseModel

router = APIRouter(prefix="/maintenance")

router.include_router(privilege.router)


@router.get("")
async def get() -> MaintenanceResponseModel:
    return MaintenanceResponseModel(maintenance=False)
