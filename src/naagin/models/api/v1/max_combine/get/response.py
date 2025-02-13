from datetime import datetime

from naagin.models.base import CustomBaseModel


class MaxCombineSwimsuitModel(CustomBaseModel):
    item_mid: int
    variation: int
    created_at: datetime


class MaxCombineGetResponseModel(CustomBaseModel):
    max_combine_swimsuit_list: list[MaxCombineSwimsuitModel]
