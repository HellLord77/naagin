from naagin.models.base import BaseModel
from naagin.models.common import BromideModel


class BromideGetResponseModel(BaseModel):
    bromide_list: list[BromideModel]
