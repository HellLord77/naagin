from datetime import datetime

from naagin.models.base import BaseModel


class HonorModel(BaseModel):
    honor_mid: int
    times_received: int
    parent_honor_mid: int
    created_at: datetime


class HonorGetResponseModel(BaseModel):
    honor_list: list[HonorModel]
