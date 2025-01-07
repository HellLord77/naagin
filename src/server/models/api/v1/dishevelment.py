from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class DishevelmentSwimsuitModel(BaseModel):
    item_mid: int
    variation: int
    created_at: datetime


class DishevelmentResponseModel(BaseModel):
    dishevelment_swimsuit_list: list[DishevelmentSwimsuitModel]

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "dishevelment_swimsuit_list": [
                        {
                            "item_mid": 426,
                            "variation": 1,
                            "created_at": "2020-04-25 05:55:51",
                        },
                        {
                            "item_mid": 427,
                            "variation": 1,
                            "created_at": "2021-04-06 07:22:23",
                        },
                        {
                            "item_mid": 431,
                            "variation": 1,
                            "created_at": "2020-10-25 04:56:35",
                        },
                        {
                            "item_mid": 432,
                            "variation": 1,
                            "created_at": "2021-04-06 07:23:09",
                        },
                        {
                            "item_mid": 434,
                            "variation": 1,
                            "created_at": "2019-12-05 09:04:33",
                        },
                        {
                            "item_mid": 460,
                            "variation": 1,
                            "created_at": "2021-04-06 07:22:51",
                        },
                        {
                            "item_mid": 934,
                            "variation": 1,
                            "created_at": "2020-08-16 08:59:46",
                        },
                    ]
                }
            ],
        }
    )
