from fastapi import APIRouter

from naagin import loggers
from naagin import settings
from naagin.models.api01 import JohrenAuthJohrenOnetimeTokenGetResponseModel

router = APIRouter(prefix="/{onetime_token}")


@router.get("")
async def get(onetime_token: str) -> JohrenAuthJohrenOnetimeTokenGetResponseModel:
    url = f"v1/johren/authJohren/{onetime_token}"
    loggers.api01.info("GET: %s", url)
    response = await settings.api01.client.get(url)
    response.raise_for_status()
    return JohrenAuthJohrenOnetimeTokenGetResponseModel.model_validate_json(response.content)
