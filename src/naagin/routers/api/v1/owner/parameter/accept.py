from fastapi import APIRouter

from naagin.models.api import OwnerParameterAcceptPostResponseModel

router = APIRouter(prefix="/accept")


@router.post("")
async def post() -> OwnerParameterAcceptPostResponseModel:
    return OwnerParameterAcceptPostResponseModel(root=[])
