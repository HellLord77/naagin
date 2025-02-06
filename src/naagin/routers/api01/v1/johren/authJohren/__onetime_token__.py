from fastapi import APIRouter

from naagin.models.api01 import JohrenAuthJohrenOnetimeTokenGetResponse

router = APIRouter(prefix="/{onetime_token}")


@router.get("")
async def get(onetime_token: str) -> JohrenAuthJohrenOnetimeTokenGetResponse:
    raise NotImplementedError
