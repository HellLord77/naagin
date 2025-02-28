from fastapi import APIRouter

from naagin.models.api import OwnerCheckLoginGetResponseModel

router = APIRouter(prefix="/checklogin")


@router.get("")
async def get() -> OwnerCheckLoginGetResponseModel:
    return OwnerCheckLoginGetResponseModel(restart_required=False)
