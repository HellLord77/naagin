from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class CustomRoomGetRequestModel(BaseModel):
    owner_id: int
    request_mid: int
    girl_mid1: int
    girl_mid2: int
    trend_status: int
    created_at: datetime
    updated_at: datetime
    started_at: datetime
    end_at: datetime


class RoomRequestGetResponseModel(BaseModel):
    custom_room_request_list: list[CustomRoomGetRequestModel]

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "custom_room_request_list": [
                        {
                            "owner_id": 288696,
                            "request_mid": 7,
                            "girl_mid1": 16,
                            "girl_mid2": 3,
                            "trend_status": 0,
                            "created_at": "2019-12-14 06:36:30",
                            "updated_at": "2024-12-30 07:58:53",
                            "started_at": "2024-12-30 07:58:53",
                            "end_at": "2024-12-31 03:58:53",
                        }
                    ]
                }
            ],
        }
    )
