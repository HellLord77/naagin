from naagin.models.base import CustomBaseModel
from naagin.models.common import FurnitureMySetModel


class FurnitureMySetGetResponseModel(CustomBaseModel):
    furniture_myset_list: list[FurnitureMySetModel]
