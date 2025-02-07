from datetime import datetime

from naagin.models.base import BaseModel


class YwrkSkillModel(BaseModel):
    id: int
    girl_mid: int
    item_mid: int
    skill_mid: int
    value: int
    created_at: datetime
    updated_at: datetime | None


class GirlYwrkSkillGetResponseModel(BaseModel):
    ywrk_skill_list: list[YwrkSkillModel]
