from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class GirlEquipmentModel(BaseModel):
    owner_id: int
    girl_mid: int
    swimsuit_equipment_item_id: int
    accessory_head_equipment_item_id: int
    accessory_face_equipment_item_id: int
    accessory_arm_equipment_item_id: int
    created_at: datetime
    updated_at: Optional[datetime]


class PvpGirlEquipmentResponseModel(BaseModel):
    pvp_girl_equipment_list: list[GirlEquipmentModel]

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "pvp_girl_equipment_list": [
                        {
                            "owner_id": 288696,
                            "girl_mid": 2,
                            "swimsuit_equipment_item_id": 109845487,
                            "accessory_head_equipment_item_id": 0,
                            "accessory_face_equipment_item_id": 0,
                            "accessory_arm_equipment_item_id": 0,
                            "created_at": "2023-03-22 19:15:47",
                            "updated_at": None,
                        },
                        {
                            "owner_id": 288696,
                            "girl_mid": 3,
                            "swimsuit_equipment_item_id": 70087563,
                            "accessory_head_equipment_item_id": 64002556,
                            "accessory_face_equipment_item_id": 66107498,
                            "accessory_arm_equipment_item_id": 62509126,
                            "created_at": "2023-03-22 19:15:47",
                            "updated_at": None,
                        },
                        {
                            "owner_id": 288696,
                            "girl_mid": 4,
                            "swimsuit_equipment_item_id": 225326892,
                            "accessory_head_equipment_item_id": 0,
                            "accessory_face_equipment_item_id": 0,
                            "accessory_arm_equipment_item_id": 0,
                            "created_at": "2023-03-22 19:15:47",
                            "updated_at": None,
                        },
                        {
                            "owner_id": 288696,
                            "girl_mid": 5,
                            "swimsuit_equipment_item_id": 69476095,
                            "accessory_head_equipment_item_id": 0,
                            "accessory_face_equipment_item_id": 0,
                            "accessory_arm_equipment_item_id": 0,
                            "created_at": "2023-03-22 19:15:47",
                            "updated_at": None,
                        },
                        {
                            "owner_id": 288696,
                            "girl_mid": 6,
                            "swimsuit_equipment_item_id": 65465327,
                            "accessory_head_equipment_item_id": 0,
                            "accessory_face_equipment_item_id": 0,
                            "accessory_arm_equipment_item_id": 0,
                            "created_at": "2023-03-22 19:15:47",
                            "updated_at": None,
                        },
                        {
                            "owner_id": 288696,
                            "girl_mid": 7,
                            "swimsuit_equipment_item_id": 179278468,
                            "accessory_head_equipment_item_id": 0,
                            "accessory_face_equipment_item_id": 0,
                            "accessory_arm_equipment_item_id": 0,
                            "created_at": "2023-03-22 19:15:47",
                            "updated_at": None,
                        },
                        {
                            "owner_id": 288696,
                            "girl_mid": 8,
                            "swimsuit_equipment_item_id": 312613976,
                            "accessory_head_equipment_item_id": 0,
                            "accessory_face_equipment_item_id": 0,
                            "accessory_arm_equipment_item_id": 0,
                            "created_at": "2023-03-22 19:15:47",
                            "updated_at": None,
                        },
                        {
                            "owner_id": 288696,
                            "girl_mid": 9,
                            "swimsuit_equipment_item_id": 207697414,
                            "accessory_head_equipment_item_id": 568839669,
                            "accessory_face_equipment_item_id": 574314209,
                            "accessory_arm_equipment_item_id": 274382667,
                            "created_at": "2023-03-22 19:15:47",
                            "updated_at": None,
                        },
                        {
                            "owner_id": 288696,
                            "girl_mid": 10,
                            "swimsuit_equipment_item_id": 248876127,
                            "accessory_head_equipment_item_id": 0,
                            "accessory_face_equipment_item_id": 0,
                            "accessory_arm_equipment_item_id": 0,
                            "created_at": "2023-03-22 19:15:47",
                            "updated_at": None,
                        },
                        {
                            "owner_id": 288696,
                            "girl_mid": 11,
                            "swimsuit_equipment_item_id": 275725128,
                            "accessory_head_equipment_item_id": 274379570,
                            "accessory_face_equipment_item_id": 70952660,
                            "accessory_arm_equipment_item_id": 62505589,
                            "created_at": "2023-03-22 19:15:47",
                            "updated_at": None,
                        },
                        {
                            "owner_id": 288696,
                            "girl_mid": 12,
                            "swimsuit_equipment_item_id": 67323522,
                            "accessory_head_equipment_item_id": 568839673,
                            "accessory_face_equipment_item_id": 70952498,
                            "accessory_arm_equipment_item_id": 69493354,
                            "created_at": "2023-03-22 19:15:47",
                            "updated_at": None,
                        },
                        {
                            "owner_id": 288696,
                            "girl_mid": 13,
                            "swimsuit_equipment_item_id": 568765745,
                            "accessory_head_equipment_item_id": 0,
                            "accessory_face_equipment_item_id": 0,
                            "accessory_arm_equipment_item_id": 0,
                            "created_at": "2023-03-22 19:15:47",
                            "updated_at": None,
                        },
                        {
                            "owner_id": 288696,
                            "girl_mid": 14,
                            "swimsuit_equipment_item_id": 362992963,
                            "accessory_head_equipment_item_id": 0,
                            "accessory_face_equipment_item_id": 0,
                            "accessory_arm_equipment_item_id": 0,
                            "created_at": "2023-03-22 19:15:47",
                            "updated_at": None,
                        },
                        {
                            "owner_id": 288696,
                            "girl_mid": 16,
                            "swimsuit_equipment_item_id": 399085510,
                            "accessory_head_equipment_item_id": 568839676,
                            "accessory_face_equipment_item_id": 1083195427,
                            "accessory_arm_equipment_item_id": 831114287,
                            "created_at": "2023-03-22 19:15:47",
                            "updated_at": None,
                        },
                        {
                            "owner_id": 288696,
                            "girl_mid": 23,
                            "swimsuit_equipment_item_id": 1526877783,
                            "accessory_head_equipment_item_id": 0,
                            "accessory_face_equipment_item_id": 0,
                            "accessory_arm_equipment_item_id": 0,
                            "created_at": "2023-08-13 19:16:32",
                            "updated_at": None,
                        },
                    ]
                }
            ],
        }
    )
