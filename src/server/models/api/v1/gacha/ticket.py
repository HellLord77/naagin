from pydantic import BaseModel
from pydantic import ConfigDict


class GachaTicketModel(BaseModel):
    item_mid: int
    count: int


class GachaTicketGetResponseModel(BaseModel):
    gacha_ticket_list: list[GachaTicketModel]

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "gacha_ticket_list": [
                        {"item_mid": 35015, "count": 88},
                        {"item_mid": 35012, "count": 16},
                        {"item_mid": 35017, "count": 4},
                        {"item_mid": 36053, "count": 3},
                        {"item_mid": 36624, "count": 2},
                        {"item_mid": 36625, "count": 2},
                        {"item_mid": 36626, "count": 2},
                        {"item_mid": 36614, "count": 2},
                        {"item_mid": 36621, "count": 1},
                        {"item_mid": 36856, "count": 1},
                        {"item_mid": 37401, "count": 10},
                        {"item_mid": 36629, "count": 78},
                        {"item_mid": 37629, "count": 3},
                        {"item_mid": 36628, "count": 2},
                        {"item_mid": 37861, "count": 5},
                        {"item_mid": 38431, "count": 1},
                        {"item_mid": 39017, "count": 2},
                    ]
                }
            ],
        }
    )
