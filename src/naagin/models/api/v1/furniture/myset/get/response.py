from naagin.models.base import BaseModel
from naagin.models.common import FurnitureMySetModel


class FurnitureMySetGetResponseModel(BaseModel):
    furniture_myset_list: list[FurnitureMySetModel]
