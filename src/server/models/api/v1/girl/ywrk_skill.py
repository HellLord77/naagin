from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class YwrkSkillModel(BaseModel):
    id: int
    girl_mid: int
    item_mid: int
    skill_mid: int
    value: int
    created_at: datetime
    updated_at: Optional  # TODO


class GirlYwrkSkillResponseModel(BaseModel):
    ywrk_skill_list: list[YwrkSkillModel]

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "ywrk_skill_list": [
                        {
                            "id": 1754966,
                            "girl_mid": 6,
                            "item_mid": 35712,
                            "skill_mid": 59,
                            "value": 5,
                            "created_at": "2020-03-23 03:12:11",
                            "updated_at": None,
                        },
                        {
                            "id": 5995099,
                            "girl_mid": 16,
                            "item_mid": 36770,
                            "skill_mid": 59,
                            "value": 5,
                            "created_at": "2022-01-12 10:58:31",
                            "updated_at": None,
                        },
                        {
                            "id": 7409427,
                            "girl_mid": 16,
                            "item_mid": 37839,
                            "skill_mid": 59,
                            "value": 5,
                            "created_at": "2022-09-01 04:42:48",
                            "updated_at": None,
                        },
                    ]
                }
            ],
        }
    )
