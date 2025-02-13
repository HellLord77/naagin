from datetime import datetime

from naagin.bases import ModelBase


class YwrkSkillModel(ModelBase):
    id: int
    girl_mid: int
    item_mid: int
    skill_mid: int
    value: int
    created_at: datetime
    updated_at: datetime | None


class GirlYwrkSkillGetResponseModel(ModelBase):
    ywrk_skill_list: list[YwrkSkillModel]
