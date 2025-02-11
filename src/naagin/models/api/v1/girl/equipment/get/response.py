from naagin.models.base import BaseModel
from naagin.models.common import GirlEquipmentModel


class GirlEquipmentGetResponseModel(BaseModel):
    girl_equipment_list: list[GirlEquipmentModel]
