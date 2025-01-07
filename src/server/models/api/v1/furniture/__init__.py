from pydantic import BaseModel
from pydantic import ConfigDict


class ItemFurnitureModel(BaseModel):
    item_mid: int
    count: int


class FurnitureGetResponseModel(BaseModel):
    item_furniture_list: list[ItemFurnitureModel]

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "item_furniture_list": [
                        {"item_mid": 45001, "count": 1},
                        {"item_mid": 45017, "count": 1},
                        {"item_mid": 45113, "count": 1},
                        {"item_mid": 45194, "count": 1},
                        {"item_mid": 45255, "count": 1},
                    ]
                }
            ],
        }
    )
