from naagin.models.base import CustomBaseModel
from naagin.models.common import GirlEquipmentModel


class GirlEquipmentGetResponseModel(CustomBaseModel):
    girl_equipment_list: list[GirlEquipmentModel]
