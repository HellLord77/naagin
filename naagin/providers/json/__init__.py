from naagin import settings
from naagin.decorators import async_lru_cache
from naagin.models.json import CSVListModel
from naagin.models.json import ResourceFileListModel
from naagin.types_.headers import ApplicationVersionHeader
from naagin.types_.headers import MasterVersionHeader

from .utils import get_bytes


@async_lru_cache
async def provide_resource_list(application_version: ApplicationVersionHeader | None = None) -> ResourceFileListModel:
    directory = settings.data.api01_dir / "v1" / "resource" / "list"
    bytes_ = await get_bytes(directory, application_version)
    return ResourceFileListModel.model_validate_json(bytes_)


@async_lru_cache
async def provide_resource_list_encrypt(
    application_version: ApplicationVersionHeader | None = None,
) -> ResourceFileListModel:
    directory = settings.data.api01_dir / "v1" / "resource" / "list" / "encrypt"
    bytes_ = await get_bytes(directory, application_version)
    return ResourceFileListModel.model_validate_json(bytes_)


@async_lru_cache
async def provide_csv_list(
    master_version: MasterVersionHeader, application_version: ApplicationVersionHeader
) -> CSVListModel:
    path = settings.data.api_dir / "v1" / "csv" / "list" / str(master_version) / f"{application_version}.json"
    bytes_ = await path.read_bytes()
    return CSVListModel.model_validate_json(bytes_)
