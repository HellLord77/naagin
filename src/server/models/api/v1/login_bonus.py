from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class LoginBonusModel(BaseModel):
    owner_id: int
    bonus_mid: int
    count: int
    complite: int
    received_at: datetime
    created_at: datetime
    updated_at: Optional[datetime]


class LoginBonusResponseModel(BaseModel):
    login_bonus_list: list[LoginBonusModel]

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "login_bonus_list": [
                        {
                            "owner_id": 288696,
                            "bonus_mid": 1,
                            "count": 4,
                            "complite": 7,
                            "received_at": "2025-01-06 19:05:03",
                            "created_at": "2019-08-01 05:36:10",
                            "updated_at": "2025-01-06 19:05:03",
                        },
                        {
                            "owner_id": 288696,
                            "bonus_mid": 58,
                            "count": 1,
                            "complite": 1,
                            "received_at": "2020-11-08 04:01:07",
                            "created_at": "2020-11-08 04:01:07",
                            "updated_at": None,
                        },
                        {
                            "owner_id": 288696,
                            "bonus_mid": 584,
                            "count": 6,
                            "complite": 0,
                            "received_at": "2025-01-06 19:05:03",
                            "created_at": "2024-12-30 07:54:59",
                            "updated_at": "2025-01-06 19:05:03",
                        },
                        {
                            "owner_id": 288696,
                            "bonus_mid": 585,
                            "count": 6,
                            "complite": 0,
                            "received_at": "2025-01-06 19:05:03",
                            "created_at": "2024-12-30 07:54:59",
                            "updated_at": "2025-01-06 19:05:03",
                        },
                        {
                            "owner_id": 288696,
                            "bonus_mid": 586,
                            "count": 1,
                            "complite": 1,
                            "received_at": "2024-12-30 07:54:59",
                            "created_at": "2024-12-30 07:54:59",
                            "updated_at": None,
                        },
                        {
                            "owner_id": 288696,
                            "bonus_mid": 587,
                            "count": 5,
                            "complite": 0,
                            "received_at": "2025-01-06 19:05:03",
                            "created_at": "2025-01-01 16:31:28",
                            "updated_at": "2025-01-06 19:05:03",
                        },
                        {
                            "owner_id": 288696,
                            "bonus_mid": 588,
                            "count": 1,
                            "complite": 1,
                            "received_at": "2025-01-01 16:31:28",
                            "created_at": "2025-01-01 16:31:28",
                            "updated_at": None,
                        },
                        {
                            "owner_id": 288696,
                            "bonus_mid": 589,
                            "count": 6,
                            "complite": 0,
                            "received_at": "2025-01-06 19:05:03",
                            "created_at": "2024-12-30 07:54:59",
                            "updated_at": "2025-01-06 19:05:03",
                        },
                        {
                            "owner_id": 288696,
                            "bonus_mid": 590,
                            "count": 2,
                            "complite": 0,
                            "received_at": "2025-01-06 19:05:03",
                            "created_at": "2025-01-06 15:48:07",
                            "updated_at": "2025-01-06 19:05:03",
                        },
                        {
                            "owner_id": 288696,
                            "bonus_mid": 591,
                            "count": 2,
                            "complite": 0,
                            "received_at": "2025-01-06 19:05:03",
                            "created_at": "2025-01-06 15:48:07",
                            "updated_at": "2025-01-06 19:05:03",
                        },
                    ]
                }
            ],
        }
    )
