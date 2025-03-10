from datetime import datetime

from naagin.bases import ModelBase


class DishevelmentSwimsuitModel(ModelBase):
    item_mid: int
    variation: int
    created_at: datetime


class DishevelmentGetResponseModel(ModelBase):
    dishevelment_swimsuit_list: list[DishevelmentSwimsuitModel]
