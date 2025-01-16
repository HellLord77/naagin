from fastapi import APIRouter

from naagin.models.api01 import MaintenancePrivilegeCheckGetResponseModel

router = APIRouter(prefix="/check")


@router.get("/{steam_id}")
async def get(
    steam_id: int,
) -> MaintenancePrivilegeCheckGetResponseModel:
    return MaintenancePrivilegeCheckGetResponseModel(result="NG")
