from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class OwnerModel(BaseModel):
    owner_id: int
    status: int
    name: str
    island_name: str
    message: str
    team_id: int
    honor1_mid: int
    honor2_mid: int
    level: int
    experience: int
    stamina: int
    main_girl_mid: int
    lend_girl_mid: int
    spot_mid: int
    spot_phase_mid: int
    license_point: int
    license_level: int
    checked_license_level: int
    birthday: Optional  #  TODO
    stamina_checked_at: datetime
    last_logged_at: datetime
    friend_code: str
    created_at: datetime


class OwnerUpdateLoginPostResponseModel(BaseModel):
    owner_list: list[OwnerModel]

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "owner_list": [
                        {
                            "owner_id": 288696,
                            "status": 3,
                            "name": "HellLord",
                            "island_name": "Venus Island",
                            "message": "Hello!",
                            "team_id": 0,
                            "honor1_mid": 340,
                            "honor2_mid": 41,
                            "level": 37,
                            "experience": 4820,
                            "stamina": 215,
                            "main_girl_mid": 16,
                            "lend_girl_mid": 12,
                            "spot_mid": 0,
                            "spot_phase_mid": 0,
                            "license_point": 12480,
                            "license_level": 10,
                            "checked_license_level": 8,
                            "birthday": None,
                            "stamina_checked_at": "2024-07-17 06:09:13",
                            "last_logged_at": "2025-01-07 08:42:26",
                            "friend_code": "034-395-513",
                            "created_at": "2019-08-01 04:52:19",
                        }
                    ]
                }
            ],
        }
    )
