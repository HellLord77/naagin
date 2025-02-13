from naagin.models.base import CustomBaseModel
from naagin.models.common import BromideModel


class BromideGetResponseModel(CustomBaseModel):
    bromide_list: list[BromideModel]
