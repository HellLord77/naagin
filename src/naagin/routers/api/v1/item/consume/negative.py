from fastapi import APIRouter

from naagin.models.api import ItemConsumeNegativeGetResponseModel

router = APIRouter(prefix="/negative")


@router.get("")
async def get() -> ItemConsumeNegativeGetResponseModel:
    return ItemConsumeNegativeGetResponseModel(item_negative_consume_list=[])
