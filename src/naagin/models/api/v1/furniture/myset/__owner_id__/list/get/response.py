from naagin.models.base import BaseModel
from naagin.models.common import FurnitureMySetModel


class FurnitureMySetOwnerIdListGetResponseModel(BaseModel):
    other_furniture_myset_list: list[FurnitureMySetModel]
