from fastapi import APIRouter

from naagin import settings
from naagin.decorators import async_lru_cache
from naagin.models.api import CSVListGetResponseModel
from naagin.types_.headers import ApplicationVersionHeader
from naagin.types_.headers import MasterVersionHeader

router = APIRouter(prefix="/list")


@router.get("")
@async_lru_cache
async def get(
    master_version: MasterVersionHeader, application_version: ApplicationVersionHeader
) -> CSVListGetResponseModel:
    json_data = await (
        settings.data.api_dir / "v1" / "csv" / "list" / str(master_version) / f"{application_version}.json"
    ).read_bytes()
    return CSVListGetResponseModel.model_validate_json(json_data)
