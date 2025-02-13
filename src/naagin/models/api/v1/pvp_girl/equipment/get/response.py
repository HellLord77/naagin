from naagin.models.base import CustomBaseModel
from naagin.models.common import GirlEquipmentModel


class PvpGirlEquipmentGetResponseModel(CustomBaseModel):
    pvp_girl_equipment_list: list[GirlEquipmentModel]
