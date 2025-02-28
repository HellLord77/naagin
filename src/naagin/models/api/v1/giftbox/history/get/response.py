from datetime import datetime

from naagin.bases import ModelBase


class GiftBoxHistoryModel(ModelBase):
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
    accepted_at: datetime


class GiftBoxHistoryGetResponseModel(ModelBase):
    giftbox_history_list: list[GiftBoxHistoryModel]
