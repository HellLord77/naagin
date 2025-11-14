from fastapi import APIRouter

from naagin.models.api01 import MaintenancePrivilegeCheckPlatformIdGetResponseModel

router = APIRouter(prefix="/{platform_id}")


@router.get("")
async def get(
    platform_id: int,  # noqa: ARG001
) -> MaintenancePrivilegeCheckPlatformIdGetResponseModel:
    return MaintenancePrivilegeCheckPlatformIdGetResponseModel(result="NG")
