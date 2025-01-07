from pydantic import BaseModel
from pydantic import ConfigDict


class ItemSealModel(BaseModel):
    id: int
    item_mid: int
    type: int
    base_mid: int
    pvp_base_mid: int
    in_lock: int
    skill_level: int
    cost: int
    rarity: int
    experience: int


class SealGetResponseModel(BaseModel):
    item_seal_list: list[ItemSealModel]

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "item_seal_list": [
                        {
                            "id": 17662198,
                            "item_mid": 30850,
                            "type": 70,
                            "base_mid": 0,
                            "pvp_base_mid": 0,
                            "in_lock": 0,
                            "skill_level": 1,
                            "cost": 15,
                            "rarity": 4,
                            "experience": 0,
                        },
                        {
                            "id": 17662199,
                            "item_mid": 30844,
                            "type": 70,
                            "base_mid": 0,
                            "pvp_base_mid": 0,
                            "in_lock": 0,
                            "skill_level": 1,
                            "cost": 15,
                            "rarity": 4,
                            "experience": 0,
                        },
                        {
                            "id": 17721927,
                            "item_mid": 30838,
                            "type": 70,
                            "base_mid": 0,
                            "pvp_base_mid": 0,
                            "in_lock": 0,
                            "skill_level": 1,
                            "cost": 15,
                            "rarity": 4,
                            "experience": 0,
                        },
                        {
                            "id": 17722249,
                            "item_mid": 30852,
                            "type": 70,
                            "base_mid": 0,
                            "pvp_base_mid": 0,
                            "in_lock": 0,
                            "skill_level": 1,
                            "cost": 15,
                            "rarity": 4,
                            "experience": 0,
                        },
                        {
                            "id": 17722250,
                            "item_mid": 30587,
                            "type": 69,
                            "base_mid": 0,
                            "pvp_base_mid": 0,
                            "in_lock": 0,
                            "skill_level": 1,
                            "cost": 20,
                            "rarity": 3,
                            "experience": 0,
                        },
                        {
                            "id": 18197383,
                            "item_mid": 30853,
                            "type": 70,
                            "base_mid": 15,
                            "pvp_base_mid": 15,
                            "in_lock": 0,
                            "skill_level": 1,
                            "cost": 15,
                            "rarity": 4,
                            "experience": 0,
                        },
                        {
                            "id": 32350481,
                            "item_mid": 30647,
                            "type": 69,
                            "base_mid": 0,
                            "pvp_base_mid": 0,
                            "in_lock": 0,
                            "skill_level": 1,
                            "cost": 20,
                            "rarity": 3,
                            "experience": 0,
                        },
                        {
                            "id": 41617669,
                            "item_mid": 30666,
                            "type": 69,
                            "base_mid": 0,
                            "pvp_base_mid": 0,
                            "in_lock": 0,
                            "skill_level": 1,
                            "cost": 20,
                            "rarity": 2,
                            "experience": 0,
                        },
                        {
                            "id": 41617670,
                            "item_mid": 30645,
                            "type": 69,
                            "base_mid": 0,
                            "pvp_base_mid": 0,
                            "in_lock": 0,
                            "skill_level": 1,
                            "cost": 20,
                            "rarity": 2,
                            "experience": 0,
                        },
                        {
                            "id": 41617671,
                            "item_mid": 31387,
                            "type": 69,
                            "base_mid": 0,
                            "pvp_base_mid": 0,
                            "in_lock": 0,
                            "skill_level": 1,
                            "cost": 20,
                            "rarity": 2,
                            "experience": 0,
                        },
                        {
                            "id": 41617806,
                            "item_mid": 31383,
                            "type": 69,
                            "base_mid": 0,
                            "pvp_base_mid": 0,
                            "in_lock": 0,
                            "skill_level": 1,
                            "cost": 20,
                            "rarity": 3,
                            "experience": 0,
                        },
                        {
                            "id": 56213249,
                            "item_mid": 31612,
                            "type": 69,
                            "base_mid": 0,
                            "pvp_base_mid": 0,
                            "in_lock": 0,
                            "skill_level": 1,
                            "cost": 20,
                            "rarity": 2,
                            "experience": 0,
                        },
                        {
                            "id": 56269636,
                            "item_mid": 30591,
                            "type": 69,
                            "base_mid": 0,
                            "pvp_base_mid": 0,
                            "in_lock": 0,
                            "skill_level": 1,
                            "cost": 20,
                            "rarity": 2,
                            "experience": 0,
                        },
                        {
                            "id": 57053565,
                            "item_mid": 31615,
                            "type": 69,
                            "base_mid": 0,
                            "pvp_base_mid": 0,
                            "in_lock": 0,
                            "skill_level": 1,
                            "cost": 20,
                            "rarity": 2,
                            "experience": 0,
                        },
                        {
                            "id": 57394822,
                            "item_mid": 31122,
                            "type": 69,
                            "base_mid": 0,
                            "pvp_base_mid": 0,
                            "in_lock": 0,
                            "skill_level": 1,
                            "cost": 20,
                            "rarity": 2,
                            "experience": 0,
                        },
                        {
                            "id": 58375965,
                            "item_mid": 30687,
                            "type": 69,
                            "base_mid": 0,
                            "pvp_base_mid": 0,
                            "in_lock": 0,
                            "skill_level": 1,
                            "cost": 20,
                            "rarity": 2,
                            "experience": 0,
                        },
                    ]
                }
            ],
        }
    )
