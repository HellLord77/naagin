from pydantic import BaseModel
from pydantic import ConfigDict


class FriendlyValueModel(BaseModel):
    girl_mid: int
    friendly_girl_mid: int
    value: int
    level: int
    unlock_count: int


class RoomGirlFriendlyGetResponseModel(BaseModel):
    friendly_value_list: list[FriendlyValueModel]

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "friendly_value_list": [
                        {
                            "girl_mid": 3,
                            "friendly_girl_mid": 7,
                            "value": 35625,
                            "level": 27,
                            "unlock_count": 0,
                        },
                        {
                            "girl_mid": 3,
                            "friendly_girl_mid": 16,
                            "value": 175205,
                            "level": 39,
                            "unlock_count": 0,
                        },
                        {
                            "girl_mid": 5,
                            "friendly_girl_mid": 7,
                            "value": 43015,
                            "level": 28,
                            "unlock_count": 0,
                        },
                        {
                            "girl_mid": 6,
                            "friendly_girl_mid": 7,
                            "value": 13745,
                            "level": 22,
                            "unlock_count": 0,
                        },
                        {
                            "girl_mid": 6,
                            "friendly_girl_mid": 12,
                            "value": 16910,
                            "level": 23,
                            "unlock_count": 0,
                        },
                        {
                            "girl_mid": 7,
                            "friendly_girl_mid": 12,
                            "value": 25,
                            "level": 2,
                            "unlock_count": 0,
                        },
                        {
                            "girl_mid": 7,
                            "friendly_girl_mid": 16,
                            "value": 94550,
                            "level": 33,
                            "unlock_count": 0,
                        },
                        {
                            "girl_mid": 11,
                            "friendly_girl_mid": 16,
                            "value": 84667,
                            "level": 33,
                            "unlock_count": 0,
                        },
                    ]
                }
            ],
        }
    )
