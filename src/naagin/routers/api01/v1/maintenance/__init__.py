from fastapi import APIRouter
from sqlalchemy import func

from naagin.models.api01 import MaintenanceGetResponseModel
from naagin.schemas import MaintenanceSchema
from naagin.types.dependencies import SessionDependency

from . import privilege

router = APIRouter(prefix="/maintenance")

router.include_router(privilege.router)


@router.get("")
async def get(session: SessionDependency) -> MaintenanceGetResponseModel:
    maintenance = await session.find(
        MaintenanceSchema, func.current_timestamp().between(MaintenanceSchema.started_at, MaintenanceSchema.end_at)
    )

    if maintenance is None:
        return MaintenanceGetResponseModel(maintenance=False)
    started_at = maintenance.started_at.strftime("%Y/%m/%d %H:%M:%S")
    end_at = maintenance.started_at.strftime("%Y/%m/%d %H:%M:%S")
    return MaintenanceGetResponseModel(maintenance=True, maintenance_datetime=f"{started_at} ~ {end_at}")
