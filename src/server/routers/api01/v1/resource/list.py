from async_lru import alru_cache
from fastapi import APIRouter

from ..... import settings
from .....models.api01 import ResourceListGetResponseModel

router = APIRouter(prefix="/list")


@router.get("")
@alru_cache
async def get() -> ResourceListGetResponseModel:
    json_data = await (
        settings.data.api01_dir
        / "v1"
        / "resource"
        / "list"
        / f"{settings.api01.game_version}.json"
    ).read_bytes()
    return ResourceListGetResponseModel.model_validate_json(json_data)
