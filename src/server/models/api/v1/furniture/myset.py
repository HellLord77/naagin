from pydantic import BaseModel
from pydantic import ConfigDict


class FurnitureMysetModel(BaseModel):
    id: int
    item_mid: int
    layout_mid: int
    rot_y: int


class FurnitureMysetResponseModel(BaseModel):
    furniture_myset_list: list[FurnitureMysetModel]

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "furniture_myset_list": [
                        {"id": 800107, "item_mid": 45001, "layout_mid": 28, "rot_y": 0},
                        {"id": 800108, "item_mid": 45017, "layout_mid": 29, "rot_y": 0},
                        {"id": 800109, "item_mid": 45194, "layout_mid": 24, "rot_y": 0},
                        {"id": 2665409, "item_mid": 45255, "layout_mid": 3, "rot_y": 0},
                        {"id": 5730462, "item_mid": 45113, "layout_mid": 1, "rot_y": 0},
                    ]
                }
            ],
        }
    )
