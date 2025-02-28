from datetime import datetime

from naagin.bases import ModelBase
from naagin.models import OwnerCheckedAtModel


class GiftBoxFetchModel(ModelBase):
    id: int
    sender_id: int
    sender_name: str
    item_mid: int
    count: int
    message_type: int
    message: str
    parameter1: int
    created_at: datetime
    expired_at: datetime
    accepted_at: None


class GiftBoxFetchPostResponseModel(ModelBase):
    giftbox_fetch_list: list[GiftBoxFetchModel]
    owner_checked_at_list: list[OwnerCheckedAtModel] | None = None
