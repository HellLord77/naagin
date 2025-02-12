from datetime import datetime

from naagin.models.base import BaseModel


class MaxCombineSwimsuitModel(BaseModel):
    item_mid: int
    variation: int
    created_at: datetime


class MaxCombineGetResponseModel(BaseModel):
    max_combine_swimsuit_list: list[MaxCombineSwimsuitModel]
