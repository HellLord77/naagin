from naagin.models.base import BaseModel
from naagin.models.utils import BromideModel


class BromideGetResponseModel(BaseModel):
    bromide_list: list[BromideModel]
