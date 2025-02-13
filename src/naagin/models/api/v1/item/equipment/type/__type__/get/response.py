from naagin.models.base import CustomBaseModel


class ItemEquipmentModel(CustomBaseModel):
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


class ItemEquipmentTypeTypeGetResponseModel(CustomBaseModel):
    item_equipment_list: list[ItemEquipmentModel]
