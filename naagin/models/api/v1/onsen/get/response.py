from datetime import datetime

from naagin.bases import ModelBase


class OnsenInfoModel(ModelBase):
    onsen_mid: int
    status: int
    quality_mid: int
    gauge_updated_at: datetime
    gauge: int
    reward_stock_second: int
    reward_count: int
    created_at: datetime
    updated_at: datetime


class OnsenSlotModel(ModelBase):
    onsen_mid: int
    slot_id: int
    girl_mid: int
    exp_updated_at: datetime
    created_at: datetime
    updated_at: datetime


class OnsenQualityStashModel(ModelBase):
    onsen_mid: int
    quality_mid: int
    reward_stock_second: int
    reward_count: int


class OnsenGetResponseModel(ModelBase):
    onsen_info_list: list[OnsenInfoModel]
    onsen_slot_list: list[OnsenSlotModel]
    onsen_quality_stash_list: list[OnsenQualityStashModel]
