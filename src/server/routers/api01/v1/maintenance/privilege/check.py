from fastapi import APIRouter

from ......models.api01.v1.maintenance.privilege.check import (
    MaintenancePrivilegeCheckGetResponseModel,
)

router = APIRouter(prefix="/check")


@router.get("/{steam_id}")
async def get(
    steam_id: int,
) -> MaintenancePrivilegeCheckGetResponseModel:
    return MaintenancePrivilegeCheckGetResponseModel(result="NG")
