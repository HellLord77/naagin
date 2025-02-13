from datetime import datetime

from naagin.models.base import CustomBaseModel


class HonorModel(CustomBaseModel):
    honor_mid: int
    times_received: int
    parent_honor_mid: int
    created_at: datetime


class HonorGetResponseModel(CustomBaseModel):
    honor_list: list[HonorModel]
