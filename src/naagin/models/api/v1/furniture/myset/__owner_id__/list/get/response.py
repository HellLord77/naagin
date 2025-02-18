from naagin.bases import ModelBase
from naagin.models import FurnitureMySetModel


class FurnitureMySetOwnerIdListGetResponseModel(ModelBase):
    other_furniture_myset_list: list[FurnitureMySetModel]
