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


class GirlEquipmentGetResponseModel(BaseModel):
    girl_equipment_list: list[GirlEquipmentModel]

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "girl_equipment_list": [
                        {
                            "owner_id": 288696,
                            "girl_mid": 2,
                            "swimsuit_equipment_item_id": 109845487,
                            "accessory_head_equipment_item_id": 0,
                            "accessory_face_equipment_item_id": 0,
                            "accessory_arm_equipment_item_id": 0,
                            "created_at": "2019-12-05 08:38:33",
                            "updated_at": None,
                        },
                        {
                            "owner_id": 288696,
                            "girl_mid": 3,
                            "swimsuit_equipment_item_id": 70087563,
                            "accessory_head_equipment_item_id": 64002556,
                            "accessory_face_equipment_item_id": 66107498,
                            "accessory_arm_equipment_item_id": 62509126,
                            "created_at": "2019-08-01 05:19:07",
                            "updated_at": "2019-09-17 05:43:41",
                        },
                        {
                            "owner_id": 288696,
                            "girl_mid": 4,
                            "swimsuit_equipment_item_id": 225326892,
                            "accessory_head_equipment_item_id": 0,
                            "accessory_face_equipment_item_id": 0,
                            "accessory_arm_equipment_item_id": 0,
                            "created_at": "2020-04-24 03:05:51",
                            "updated_at": None,
                        },
                        {
                            "owner_id": 288696,
                            "girl_mid": 5,
                            "swimsuit_equipment_item_id": 69476095,
                            "accessory_head_equipment_item_id": 0,
                            "accessory_face_equipment_item_id": 0,
                            "accessory_arm_equipment_item_id": 0,
                            "created_at": "2019-09-14 02:51:19",
                            "updated_at": None,
                        },
                        {
                            "owner_id": 288696,
                            "girl_mid": 6,
                            "swimsuit_equipment_item_id": 65465327,
                            "accessory_head_equipment_item_id": 0,
                            "accessory_face_equipment_item_id": 0,
                            "accessory_arm_equipment_item_id": 0,
                            "created_at": "2019-08-30 13:04:36",
                            "updated_at": "2021-04-08 03:14:01",
                        },
                        {
                            "owner_id": 288696,
                            "girl_mid": 7,
                            "swimsuit_equipment_item_id": 179278468,
                            "accessory_head_equipment_item_id": 0,
                            "accessory_face_equipment_item_id": 0,
                            "accessory_arm_equipment_item_id": 0,
                            "created_at": "2020-03-17 14:12:05",
                            "updated_at": "2021-04-07 04:03:29",
                        },
                        {
                            "owner_id": 288696,
                            "girl_mid": 8,
                            "swimsuit_equipment_item_id": 312613976,
                            "accessory_head_equipment_item_id": 0,
                            "accessory_face_equipment_item_id": 0,
                            "accessory_arm_equipment_item_id": 0,
                            "created_at": "2020-07-29 10:21:57",
                            "updated_at": None,
                        },
                        {
                            "owner_id": 288696,
                            "girl_mid": 9,
                            "swimsuit_equipment_item_id": 207697414,
                            "accessory_head_equipment_item_id": 568839669,
                            "accessory_face_equipment_item_id": 574314209,
                            "accessory_arm_equipment_item_id": 274382667,
                            "created_at": "2020-04-09 08:47:49",
                            "updated_at": "2021-04-08 03:18:15",
                        },
                        {
                            "owner_id": 288696,
                            "girl_mid": 10,
                            "swimsuit_equipment_item_id": 248876127,
                            "accessory_head_equipment_item_id": 0,
                            "accessory_face_equipment_item_id": 0,
                            "accessory_arm_equipment_item_id": 0,
                            "created_at": "2020-05-16 15:50:47",
                            "updated_at": None,
                        },
                        {
                            "owner_id": 288696,
                            "girl_mid": 11,
                            "swimsuit_equipment_item_id": 275725128,
                            "accessory_head_equipment_item_id": 274379570,
                            "accessory_face_equipment_item_id": 70952660,
                            "accessory_arm_equipment_item_id": 62505589,
                            "created_at": "2019-08-01 05:29:24",
                            "updated_at": "2020-06-17 11:51:17",
                        },
                        {
                            "owner_id": 288696,
                            "girl_mid": 12,
                            "swimsuit_equipment_item_id": 67323522,
                            "accessory_head_equipment_item_id": 568839673,
                            "accessory_face_equipment_item_id": 70952498,
                            "accessory_arm_equipment_item_id": 69493354,
                            "created_at": "2019-09-05 05:08:42",
                            "updated_at": "2021-04-07 03:53:39",
                        },
                        {
                            "owner_id": 288696,
                            "girl_mid": 13,
                            "swimsuit_equipment_item_id": 568765745,
                            "accessory_head_equipment_item_id": 0,
                            "accessory_face_equipment_item_id": 0,
                            "accessory_arm_equipment_item_id": 0,
                            "created_at": "2021-04-05 03:40:30",
                            "updated_at": None,
                        },
                        {
                            "owner_id": 288696,
                            "girl_mid": 14,
                            "swimsuit_equipment_item_id": 362992963,
                            "accessory_head_equipment_item_id": 0,
                            "accessory_face_equipment_item_id": 0,
                            "accessory_arm_equipment_item_id": 0,
                            "created_at": "2020-09-24 03:31:26",
                            "updated_at": None,
                        },
                        {
                            "owner_id": 288696,
                            "girl_mid": 16,
                            "swimsuit_equipment_item_id": 399085510,
                            "accessory_head_equipment_item_id": 568839676,
                            "accessory_face_equipment_item_id": 1083195427,
                            "accessory_arm_equipment_item_id": 831114287,
                            "created_at": "2020-10-22 08:50:48",
                            "updated_at": "2022-08-18 19:08:27",
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
