from naagin.bases import ModelBase


class ItemEquipmentModel(ModelBase):
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


class ItemEquipmentTypeTypeGetResponseModel(ModelBase):
    item_equipment_list: list[ItemEquipmentModel]
