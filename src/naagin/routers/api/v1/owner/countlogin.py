from fastapi import APIRouter

from naagin.models.api import OwnerCountLoginGetResponseModel

router = APIRouter(prefix="/countlogin")


@router.get("")
async def get() -> OwnerCountLoginGetResponseModel:
    return OwnerCountLoginGetResponseModel(login_count=0)
