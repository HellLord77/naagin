import async_lru
from fastapi import APIRouter

from ..... import consts
from .....models.api01.v1.resource.list.get.response import ResourceListGetResponseModel

router = APIRouter(prefix="/list")


@router.get("")
@async_lru.alru_cache
async def get() -> ResourceListGetResponseModel:
    json_data = await (consts.API01_DIR / "v1" / "resource" / "list.json").read_bytes()
    return ResourceListGetResponseModel.model_validate_json(json_data)
