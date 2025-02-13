from datetime import datetime

from naagin.bases import ModelBase


class OwnerCheckedAtModel(ModelBase):
    owner_id: int
    news_checked_at: datetime
    quest_checked_at: datetime
    event_checked_at: datetime
    reward_notification_checked_at: datetime
    notification_checked_at: datetime
    giftbox_checked_at: datetime
    shared_giftbox_checked_at: datetime
    friendship_checked_at: datetime
    honor_checked_at: datetime
    mission_checked_at: datetime
    shared_login_bonus_checked_at: datetime | None
    subscription_checked_at: datetime | None
    lesson2onsen_exchanged_item_at: datetime | None
    comeback_login_bonus_expire_at: None
    compensation_create_girl_append_item_at: None
    created_at: datetime
    updated_at: datetime | None


class OwnerCheckedAtGetResponseModel(ModelBase):
    owner_checked_at: OwnerCheckedAtModel
