from fastapi import APIRouter

from naagin.models.api import ShopPaymentlogIncompleteGetResponseModel

router = APIRouter(prefix="/incomplete")


@router.get("")
async def get() -> ShopPaymentlogIncompleteGetResponseModel:
    return ShopPaymentlogIncompleteGetResponseModel(payment_log_list=[])
