from naagin.bases import ModelBase
from naagin.models import BgmModel


class RadioStationBgmSceneMidPostResponseModel(ModelBase):
    bgm_list: list[BgmModel]
