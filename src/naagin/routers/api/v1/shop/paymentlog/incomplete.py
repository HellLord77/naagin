from fastapi import APIRouter

from naagin.models.api import ShopPaymentLogIncompleteGetResponseModel

router = APIRouter(prefix="/incomplete")


@router.get("")
async def get() -> ShopPaymentLogIncompleteGetResponseModel:
    return ShopPaymentLogIncompleteGetResponseModel(payment_log_list=[])
