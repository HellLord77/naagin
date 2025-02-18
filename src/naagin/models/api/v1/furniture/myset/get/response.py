from naagin.bases import ModelBase
from naagin.models import FurnitureMySetModel


class FurnitureMySetGetResponseModel(ModelBase):
    furniture_myset_list: list[FurnitureMySetModel]
