from naagin.bases import ModelBase
from naagin.models import GirlEquipmentModel


class PvpGirlEquipmentGetResponseModel(ModelBase):
    pvp_girl_equipment_list: list[GirlEquipmentModel]
