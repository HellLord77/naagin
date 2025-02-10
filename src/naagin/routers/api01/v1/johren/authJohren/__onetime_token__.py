from functools import cache

from fastapi import APIRouter
from httpx import AsyncClient

from naagin import settings
from naagin.models.api01 import JohrenAuthJohrenOnetimeTokenGetResponse

router = APIRouter(prefix="/{onetime_token}")


@cache
def get_client() -> AsyncClient:
    return AsyncClient(base_url=settings.api01.base_url, trust_env=not settings.api01.no_proxy)


@router.get("")
async def get(onetime_token: str) -> JohrenAuthJohrenOnetimeTokenGetResponse:
    response = await get_client().get(f"/v1/johren/authJohren/{onetime_token}")
    response.raise_for_status()

    json_data = response.content
    return JohrenAuthJohrenOnetimeTokenGetResponse.model_validate_json(json_data)
