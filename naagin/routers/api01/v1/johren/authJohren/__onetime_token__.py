from fastapi import APIRouter

from naagin import settings
from naagin.models.api01 import JohrenAuthJohrenOnetimeTokenGetResponse

router = APIRouter(prefix="/{onetime_token}")


@router.get("")
async def get(onetime_token: str) -> JohrenAuthJohrenOnetimeTokenGetResponse:
    response = await settings.api01.client.get(f"/v1/johren/authJohren/{onetime_token}")
    response.raise_for_status()

    json_data = response.content
    return JohrenAuthJohrenOnetimeTokenGetResponse.model_validate_json(json_data)
