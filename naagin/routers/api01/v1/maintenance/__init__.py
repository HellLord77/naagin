from fastapi import APIRouter

from naagin.models.api01 import MaintenanceGetResponseModel
from naagin.types_.dependencies import MaintenanceDependency

from . import privilege

router = APIRouter(prefix="/maintenance")

router.include_router(privilege.router)


@router.get("")
async def get(maintenance: MaintenanceDependency) -> MaintenanceGetResponseModel:
    if maintenance is None:
        return MaintenanceGetResponseModel(maintenance=False)

    started_at = maintenance.started_at.strftime("%Y/%m/%d %H:%M:%S")
    end_at = maintenance.started_at.strftime("%Y/%m/%d %H:%M:%S")
    return MaintenanceGetResponseModel(maintenance=True, maintenance_datetime=f"{started_at} ~ {end_at}")
