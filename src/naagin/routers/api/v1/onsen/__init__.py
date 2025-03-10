from fastapi import APIRouter

from naagin.models.api import OnsenGetResponseModel

router = APIRouter(prefix="/onsen")


@router.get("")
async def get() -> OnsenGetResponseModel:
    return OnsenGetResponseModel(onsen_info_list=[], onsen_slot_list=[], onsen_quality_stash_list=[])
