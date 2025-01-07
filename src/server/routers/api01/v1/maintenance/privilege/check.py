from fastapi import APIRouter

from ......models.api01.v1.maintenance.privilege.check import (
    MaintenancePrivilegeCheckSteamIdGetResponseModel,
)

router = APIRouter(prefix="/check")


@router.get("/{steam_id}")
async def get_steam_id(
    steam_id: int,
) -> MaintenancePrivilegeCheckSteamIdGetResponseModel:
    return MaintenancePrivilegeCheckSteamIdGetResponseModel(result="NG")
