from naagin.bases import ModelBase
from naagin.models import BgmModel


class RadioStationBgmGetResponseModel(ModelBase):
    bgm_list: list[BgmModel]
