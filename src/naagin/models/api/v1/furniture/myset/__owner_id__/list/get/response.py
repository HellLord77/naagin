from naagin.models.base import CustomBaseModel
from naagin.models.common import FurnitureMySetModel


class FurnitureMySetOwnerIdListGetResponseModel(CustomBaseModel):
    other_furniture_myset_list: list[FurnitureMySetModel]
