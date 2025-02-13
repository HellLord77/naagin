from naagin.bases import ModelBase
from naagin.models.common import GirlEquipmentModel


class GirlEquipmentGetResponseModel(ModelBase):
    girl_equipment_list: list[GirlEquipmentModel]
