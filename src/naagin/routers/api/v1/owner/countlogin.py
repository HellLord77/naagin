from fastapi import APIRouter

from naagin.models.api import OwnerCountloginGetResponseModel

router = APIRouter(prefix="/countlogin")


@router.get("")
async def get() -> OwnerCountloginGetResponseModel:
    return OwnerCountloginGetResponseModel(login_count=0)
