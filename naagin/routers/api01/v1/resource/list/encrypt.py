from secrets import token_hex

from fastapi import APIRouter

from naagin import settings
from naagin.decorators import async_lru_cache
from naagin.models.api01 import ResourceListEncryptPostRequestModel
from naagin.models.api01 import ResourceListEncryptPostResponseModel
from naagin.models.api01 import ResourceListGetResponseModel
from naagin.utils import encrypt_resource_data

router = APIRouter(prefix="/encrypt")


@async_lru_cache
async def get_resource_list() -> bytes:
    json_data = await (
        settings.data.api01_dir / "v1" / "resource" / "list" / "encrypt" / f"{settings.version.application}.json"
    ).read_bytes()
    resource_list = ResourceListGetResponseModel.model_validate_json(json_data)
    return resource_list.model_dump_json().encode()


@router.post("")
async def post(request: ResourceListEncryptPostRequestModel) -> ResourceListEncryptPostResponseModel:
    resource_list = await get_resource_list()

    p = token_hex(16)
    resource_list_encrypt = encrypt_resource_data(request.platform_id, p.encode(), resource_list)
    return ResourceListEncryptPostResponseModel(resource_list_encrypt=resource_list_encrypt, p=p)
