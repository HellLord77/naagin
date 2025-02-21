from fastapi import APIRouter

from naagin.models.api import GirlHeadAccessorySwitchListGetResponseModel

router = APIRouter(prefix="/list")


@router.get("")
async def get() -> GirlHeadAccessorySwitchListGetResponseModel:
    return GirlHeadAccessorySwitchListGetResponseModel(head_accessary_switch_list=[])
