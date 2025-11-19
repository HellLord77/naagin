from fastapi import APIRouter

from naagin.models.api import SubscriptionGetResponseModel
from naagin.models.api.v1.subscription.get.response import SubscriptionListModel

router = APIRouter(prefix="/subscription")


@router.get("")
async def get() -> SubscriptionGetResponseModel:
    subscription_list = SubscriptionListModel(owner_fp=[0, 0], pass_details=[])
    return SubscriptionGetResponseModel(subscription_list=subscription_list)
