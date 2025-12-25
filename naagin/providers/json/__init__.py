from anyio.functools import lru_cache

from naagin import settings
from naagin.models.json import CSVListModel
from naagin.models.json import ResourceFileListModel
from naagin.types_.headers import ApplicationVersionHeader
from naagin.types_.headers import MasterVersionHeader

from .utils import get_resource_list_data


@lru_cache
async def provide_resource_list(application_version: ApplicationVersionHeader | None = None) -> ResourceFileListModel:
    data = await get_resource_list_data(application_version, encrypt=False)
    return ResourceFileListModel.model_validate_json(data)


@lru_cache
async def provide_resource_list_encrypt(
    application_version: ApplicationVersionHeader | None = None,
) -> ResourceFileListModel:
    data = await get_resource_list_data(application_version, encrypt=True)
    return ResourceFileListModel.model_validate_json(data)


@lru_cache
async def provide_csv_list(
    master_version: MasterVersionHeader, application_version: ApplicationVersionHeader
) -> CSVListModel:
    path = settings.data.api_dir / "v1" / "csv" / "list" / str(master_version) / f"{application_version}.json"
    data = await path.read_bytes()
    return CSVListModel.model_validate_json(data)
