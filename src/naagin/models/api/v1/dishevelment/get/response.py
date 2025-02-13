from datetime import datetime

from naagin.models.base import CustomBaseModel


class DishevelmentSwimsuitModel(CustomBaseModel):
    item_mid: int
    variation: int
    created_at: datetime


class DishevelmentGetResponseModel(CustomBaseModel):
    dishevelment_swimsuit_list: list[DishevelmentSwimsuitModel]
