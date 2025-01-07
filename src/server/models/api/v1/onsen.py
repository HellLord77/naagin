from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class OnsenInfoModel(BaseModel):
    onsen_mid: int
    status: int
    quality_mid: int
    gauge_updated_at: datetime
    gauge: int
    reward_stock_second: int
    reward_count: int
    created_at: datetime
    updated_at: datetime


class OnsenSlotModel(BaseModel):
    onsen_mid: int
    slot_id: int
    girl_mid: int
    exp_updated_at: datetime
    created_at: datetime
    updated_at: datetime


class OnsenResponseModel(BaseModel):
    onsen_info_list: list[OnsenInfoModel]
    onsen_slot_list: list[OnsenSlotModel]
    onsen_quality_stash_list: list  # TODO

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "onsen_info_list": [
                        {
                            "onsen_mid": 0,
                            "status": 0,
                            "quality_mid": 1,
                            "gauge_updated_at": "2024-07-17 06:01:28",
                            "gauge": 0,
                            "reward_stock_second": 0,
                            "reward_count": 25,
                            "created_at": "2023-08-13 19:22:20",
                            "updated_at": "2024-12-30 07:58:01",
                        }
                    ],
                    "onsen_slot_list": [
                        {
                            "onsen_mid": 0,
                            "slot_id": 0,
                            "girl_mid": 16,
                            "exp_updated_at": "2024-12-30 07:22:20",
                            "created_at": "2023-08-13 19:22:20",
                            "updated_at": "2024-12-30 07:58:01",
                        },
                        {
                            "onsen_mid": 0,
                            "slot_id": 1,
                            "girl_mid": 11,
                            "exp_updated_at": "2024-12-30 07:22:28",
                            "created_at": "2023-08-13 19:22:28",
                            "updated_at": "2024-12-30 07:58:01",
                        },
                        {
                            "onsen_mid": 0,
                            "slot_id": 2,
                            "girl_mid": 3,
                            "exp_updated_at": "2024-12-30 07:22:33",
                            "created_at": "2023-08-13 19:22:33",
                            "updated_at": "2024-12-30 07:58:01",
                        },
                        {
                            "onsen_mid": 0,
                            "slot_id": 3,
                            "girl_mid": 6,
                            "exp_updated_at": "2024-12-30 07:22:36",
                            "created_at": "2023-08-13 19:22:36",
                            "updated_at": "2024-12-30 07:58:01",
                        },
                    ],
                    "onsen_quality_stash_list": [],
                }
            ],
        }
    )
