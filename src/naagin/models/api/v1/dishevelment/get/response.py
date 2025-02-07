from datetime import datetime

from naagin.models.base import BaseModel


class DishevelmentSwimsuitModel(BaseModel):
    item_mid: int
    variation: int
    created_at: datetime


class DishevelmentGetResponseModel(BaseModel):
    dishevelment_swimsuit_list: list[DishevelmentSwimsuitModel]
