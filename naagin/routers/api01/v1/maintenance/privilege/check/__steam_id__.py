from fastapi import APIRouter

from naagin.models.api01 import MaintenancePrivilegeCheckSteamIdGetResponseModel

router = APIRouter(prefix="/{steam_id}")


@router.get("")
async def get(
    steam_id: int,  # noqa: ARG001
) -> MaintenancePrivilegeCheckSteamIdGetResponseModel:
    return MaintenancePrivilegeCheckSteamIdGetResponseModel(result="NG")
