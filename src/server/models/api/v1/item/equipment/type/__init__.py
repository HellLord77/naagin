from pydantic import BaseModel
from pydantic import ConfigDict


class ItemEquipmentModel(BaseModel):
    id: int
    item_mid: int
    type: int
    level: int
    experience: int
    girl_mid: int
    favorite: int
    in_lock: int
    unlock_count: int
    upgrade_count: int
    combine_count: int


class ItemEquipmentTypeResponseModel(BaseModel):
    item_equipment_list: list[ItemEquipmentModel]

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "item_equipment_list": [
                        {
                            "id": 571974653,
                            "item_mid": 52037,
                            "type": 82,
                            "level": 1,
                            "experience": 0,
                            "girl_mid": 0,
                            "favorite": 0,
                            "in_lock": 0,
                            "unlock_count": 0,
                            "upgrade_count": 0,
                            "combine_count": 0,
                        },
                        {
                            "id": 571974887,
                            "item_mid": 52052,
                            "type": 82,
                            "level": 1,
                            "experience": 0,
                            "girl_mid": 0,
                            "favorite": 0,
                            "in_lock": 0,
                            "unlock_count": 0,
                            "upgrade_count": 0,
                            "combine_count": 0,
                        },
                        {
                            "id": 571975080,
                            "item_mid": 52062,
                            "type": 82,
                            "level": 1,
                            "experience": 0,
                            "girl_mid": 0,
                            "favorite": 0,
                            "in_lock": 0,
                            "unlock_count": 0,
                            "upgrade_count": 0,
                            "combine_count": 0,
                        },
                        {
                            "id": 571975277,
                            "item_mid": 52072,
                            "type": 82,
                            "level": 1,
                            "experience": 0,
                            "girl_mid": 0,
                            "favorite": 0,
                            "in_lock": 0,
                            "unlock_count": 0,
                            "upgrade_count": 0,
                            "combine_count": 0,
                        },
                        {
                            "id": 571975504,
                            "item_mid": 52022,
                            "type": 82,
                            "level": 1,
                            "experience": 0,
                            "girl_mid": 0,
                            "favorite": 0,
                            "in_lock": 0,
                            "unlock_count": 0,
                            "upgrade_count": 0,
                            "combine_count": 0,
                        },
                        {
                            "id": 571975796,
                            "item_mid": 52027,
                            "type": 82,
                            "level": 1,
                            "experience": 0,
                            "girl_mid": 0,
                            "favorite": 0,
                            "in_lock": 0,
                            "unlock_count": 0,
                            "upgrade_count": 0,
                            "combine_count": 0,
                        },
                        {
                            "id": 571975969,
                            "item_mid": 52017,
                            "type": 82,
                            "level": 1,
                            "experience": 0,
                            "girl_mid": 0,
                            "favorite": 0,
                            "in_lock": 0,
                            "unlock_count": 0,
                            "upgrade_count": 0,
                            "combine_count": 0,
                        },
                        {
                            "id": 571976156,
                            "item_mid": 52007,
                            "type": 82,
                            "level": 1,
                            "experience": 0,
                            "girl_mid": 0,
                            "favorite": 0,
                            "in_lock": 0,
                            "unlock_count": 0,
                            "upgrade_count": 0,
                            "combine_count": 0,
                        },
                        {
                            "id": 571976347,
                            "item_mid": 52012,
                            "type": 82,
                            "level": 1,
                            "experience": 0,
                            "girl_mid": 0,
                            "favorite": 0,
                            "in_lock": 0,
                            "unlock_count": 0,
                            "upgrade_count": 0,
                            "combine_count": 0,
                        },
                        {
                            "id": 571976514,
                            "item_mid": 52047,
                            "type": 82,
                            "level": 1,
                            "experience": 0,
                            "girl_mid": 0,
                            "favorite": 0,
                            "in_lock": 0,
                            "unlock_count": 0,
                            "upgrade_count": 0,
                            "combine_count": 0,
                        },
                        {
                            "id": 571976686,
                            "item_mid": 52002,
                            "type": 82,
                            "level": 1,
                            "experience": 0,
                            "girl_mid": 0,
                            "favorite": 0,
                            "in_lock": 0,
                            "unlock_count": 0,
                            "upgrade_count": 0,
                            "combine_count": 0,
                        },
                        {
                            "id": 571976983,
                            "item_mid": 52042,
                            "type": 82,
                            "level": 1,
                            "experience": 0,
                            "girl_mid": 0,
                            "favorite": 0,
                            "in_lock": 0,
                            "unlock_count": 0,
                            "upgrade_count": 0,
                            "combine_count": 0,
                        },
                        {
                            "id": 571977186,
                            "item_mid": 52032,
                            "type": 82,
                            "level": 1,
                            "experience": 0,
                            "girl_mid": 0,
                            "favorite": 0,
                            "in_lock": 0,
                            "unlock_count": 0,
                            "upgrade_count": 0,
                            "combine_count": 0,
                        },
                        {
                            "id": 571977382,
                            "item_mid": 52057,
                            "type": 82,
                            "level": 1,
                            "experience": 0,
                            "girl_mid": 0,
                            "favorite": 0,
                            "in_lock": 0,
                            "unlock_count": 0,
                            "upgrade_count": 0,
                            "combine_count": 0,
                        },
                    ]
                }
            ],
        }
    )
