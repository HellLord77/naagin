from fastapi import APIRouter

from naagin.models.api import OwnerParameterAcceptPostResponseModel

router = APIRouter(prefix="/accept")


@router.post("")
async def get() -> OwnerParameterAcceptPostResponseModel:
    return OwnerParameterAcceptPostResponseModel(root=[])
