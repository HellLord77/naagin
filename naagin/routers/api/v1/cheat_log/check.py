from fastapi import APIRouter

from naagin.models.api import CheatLogCheckGetResponseModel

router = APIRouter(prefix="/check")


@router.get("")
async def get() -> CheatLogCheckGetResponseModel:
    return CheatLogCheckGetResponseModel(count=0)
