from datetime import datetime

from naagin.models.base import BaseModel


class PvpGirlEquipmentModel(BaseModel):
    owner_id: int
    girl_mid: int
    swimsuit_equipment_item_id: int
    accessory_head_equipment_item_id: int
    accessory_face_equipment_item_id: int
    accessory_arm_equipment_item_id: int
    created_at: datetime
    updated_at: datetime | None


class PvpGirlEquipmentGetResponseModel(BaseModel):
    pvp_girl_equipment_list: list[PvpGirlEquipmentModel]
