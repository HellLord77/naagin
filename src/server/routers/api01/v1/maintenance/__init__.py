from fastapi import APIRouter

from . import privilege
from .....models.api01 import MaintenanceGetResponseModel

router = APIRouter(prefix="/maintenance")

router.include_router(privilege.router)


@router.get("")
async def get() -> MaintenanceGetResponseModel:
    return MaintenanceGetResponseModel(maintenance=False)
