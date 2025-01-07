from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class OwnerCheckedAtModel(BaseModel):
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
    shared_login_bonus_checked_at: datetime
    subscription_checked_at: Optional  # TODO
    lesson2onsen_exchanged_item_at: datetime
    comeback_login_bonus_expire_at: Optional  # TODO
    compensation_create_girl_append_item_at: Optional  # TODO
    created_at: datetime
    updated_at: datetime


class OwnerCountLoginResponseModel(BaseModel):
    giftbox_fetch_list: list  # TODO
    owner_checked_at_list: list[OwnerCheckedAtModel]

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "giftbox_fetch_list": [],
                    "owner_checked_at_list": [
                        {
                            "owner_id": 288696,
                            "news_checked_at": "2019-08-01 04:52:19",
                            "quest_checked_at": "2019-08-01 04:52:19",
                            "event_checked_at": "2019-08-01 04:52:19",
                            "reward_notification_checked_at": "2019-08-01 04:52:19",
                            "notification_checked_at": "2019-08-01 04:52:19",
                            "giftbox_checked_at": "2019-08-01 04:52:19",
                            "shared_giftbox_checked_at": "2025-01-07 08:42:20",
                            "friendship_checked_at": "2024-12-30 08:00:42",
                            "honor_checked_at": "2025-01-07 08:42:18",
                            "mission_checked_at": "2024-10-17 14:34:18",
                            "shared_login_bonus_checked_at": "2025-01-06 19:05:03",
                            "subscription_checked_at": None,
                            "lesson2onsen_exchanged_item_at": "2023-08-13 19:11:58",
                            "comeback_login_bonus_expire_at": None,
                            "compensation_create_girl_append_item_at": None,
                            "created_at": "2019-08-01 04:52:19",
                            "updated_at": "2025-01-07 08:42:20",
                        }
                    ],
                }
            ],
        }
    )
