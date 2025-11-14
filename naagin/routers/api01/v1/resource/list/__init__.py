from fastapi import APIRouter

from naagin import settings
from naagin.decorators import async_lru_cache
from naagin.models.api01 import ResourceListGetResponseModel

from . import encrypt

router = APIRouter(prefix="/list")

router.include_router(encrypt.router)


@router.get("")
@async_lru_cache
async def get() -> ResourceListGetResponseModel:
    json_data = await (
        settings.data.api01_dir / "v1" / "resource" / "list" / f"{settings.version.application}.json"
    ).read_bytes()
    return ResourceListGetResponseModel.model_validate_json(json_data)
