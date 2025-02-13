from datetime import datetime

from naagin.models.base import CustomBaseModel


class YwrkSkillModel(CustomBaseModel):
    id: int
    girl_mid: int
    item_mid: int
    skill_mid: int
    value: int
    created_at: datetime
    updated_at: datetime | None


class GirlYwrkSkillGetResponseModel(CustomBaseModel):
    ywrk_skill_list: list[YwrkSkillModel]
