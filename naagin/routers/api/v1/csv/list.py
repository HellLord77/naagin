from async_lru import alru_cache
from fastapi import APIRouter

from naagin import settings
from naagin.models.api import CSVListGetResponseModel

router = APIRouter(prefix="/list")


@router.get("")
@alru_cache
async def get() -> CSVListGetResponseModel:
    json_data = await (
        settings.data.api_dir / "v1" / "csv" / "list" / f"{settings.version.application}.json"
    ).read_bytes()
    return CSVListGetResponseModel.model_validate_json(json_data)
