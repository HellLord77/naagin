from datetime import datetime

from naagin.bases import ModelBase


class LoginBonusModel(ModelBase):
    owner_id: int
    bonus_mid: int
    count: int
    complite: int
    received_at: datetime | None
    created_at: datetime
    updated_at: datetime | None


class LoginBonusGetResponseModel(ModelBase):
    login_bonus_list: list[LoginBonusModel]
