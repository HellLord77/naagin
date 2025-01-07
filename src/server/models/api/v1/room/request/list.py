from pydantic import BaseModel
from pydantic import ConfigDict


class CustomRoomRequestLogModel(BaseModel):
    request_mid: int
    clear_rank: int


class RoomRequestListResponseModel(BaseModel):
    custom_room_request_log_list: list[CustomRoomRequestLogModel]

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "custom_room_request_log_list": [
                        {"request_mid": 2, "clear_rank": 3},
                        {"request_mid": 3, "clear_rank": 2},
                        {"request_mid": 5, "clear_rank": 2},
                        {"request_mid": 6, "clear_rank": 3},
                        {"request_mid": 7, "clear_rank": 3},
                        {"request_mid": 8, "clear_rank": 1},
                    ]
                }
            ],
        }
    )
