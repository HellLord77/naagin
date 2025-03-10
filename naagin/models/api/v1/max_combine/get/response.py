from datetime import datetime

from naagin.bases import ModelBase


class MaxCombineSwimsuitModel(ModelBase):
    item_mid: int
    variation: int
    created_at: datetime


class MaxCombineGetResponseModel(ModelBase):
    max_combine_swimsuit_list: list[MaxCombineSwimsuitModel]
