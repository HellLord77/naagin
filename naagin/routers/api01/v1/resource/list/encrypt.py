from secrets import token_hex

from fastapi import APIRouter

from naagin.models.api01 import ResourceListEncryptPostRequestModel
from naagin.models.api01 import ResourceListEncryptPostResponseModel
from naagin.types_.dependencies.json import ResourceListEncryptDependency
from naagin.utils import encrypt_resource_data

router = APIRouter(prefix="/encrypt")


@router.post("")
async def post(
    request: ResourceListEncryptPostRequestModel, resource_list_encrypt: ResourceListEncryptDependency
) -> ResourceListEncryptPostResponseModel:
    resource_list = resource_list_encrypt.model_dump_json().encode()

    p = token_hex(16)
    resource_list_encrypt = encrypt_resource_data(request.platform_id, p.encode(), resource_list)
    return ResourceListEncryptPostResponseModel(resource_list_encrypt=resource_list_encrypt, p=p)
