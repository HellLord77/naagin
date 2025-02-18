from naagin.bases import ModelBase
from naagin.models import BromideModel


class BromideGetResponseModel(ModelBase):
    bromide_list: list[BromideModel]
