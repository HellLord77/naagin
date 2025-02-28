from fastapi import APIRouter

from naagin.models.api import GiftBoxFetchPostResponseModel

router = APIRouter(prefix="/fetch")


@router.post("")
async def post() -> GiftBoxFetchPostResponseModel:
    return GiftBoxFetchPostResponseModel(giftbox_fetch_list=[])
