from fastapi import APIRouter

from naagin.models.api01 import MaintenanceGetResponseModel
from . import privilege

router = APIRouter(prefix="/maintenance")

router.include_router(privilege.router)


@router.get("")
async def get() -> MaintenanceGetResponseModel:
    return MaintenanceGetResponseModel(maintenance=False)
