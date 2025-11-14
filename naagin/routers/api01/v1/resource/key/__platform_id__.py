from secrets import token_hex

from fastapi import APIRouter

from naagin.models.api01 import ResourceKeyPlatformIdGetResponseModel
from naagin.utils import encrypt_resource_data

router = APIRouter(prefix="/{platform_id}")


@router.get("")
async def get(platform_id: int) -> ResourceKeyPlatformIdGetResponseModel:
    key = token_hex(32).encode()

    p = token_hex(16)
    e = encrypt_resource_data(platform_id, p.encode(), key)
    return ResourceKeyPlatformIdGetResponseModel(e=e, p=p)
