from naagin.bases import ModelBase
from naagin.models.common import BromideModel


class BromideGetResponseModel(ModelBase):
    bromide_list: list[BromideModel]
