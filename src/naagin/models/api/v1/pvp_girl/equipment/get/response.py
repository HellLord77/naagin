from naagin.models.base import BaseModel
from naagin.models.common import GirlEquipmentModel


class PvpGirlEquipmentGetResponseModel(BaseModel):
    pvp_girl_equipment_list: list[GirlEquipmentModel]
