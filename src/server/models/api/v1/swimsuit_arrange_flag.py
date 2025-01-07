from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class SwimsuitArrageFlagModel(BaseModel):
    owner_id: int
    girl_mid: int
    variation: int
    switch: int
    created_at: datetime
    updated_at: datetime


class SwimsuitArrangeFlagResponseModel(BaseModel):
    swimsuit_arrage_flag_list: list[SwimsuitArrageFlagModel]

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "swimsuit_arrage_flag_list": [
                        {
                            "owner_id": 288696,
                            "girl_mid": 23,
                            "variation": 102,
                            "switch": 0,
                            "created_at": "2023-08-13 19:21:26",
                            "updated_at": "2023-08-13 19:21:32",
                        }
                    ]
                }
            ],
        }
    )
