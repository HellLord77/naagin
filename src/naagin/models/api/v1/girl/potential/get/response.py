from datetime import datetime

from naagin.bases import ModelBase


class GirlPotentialModel(ModelBase):
    owner_id: int
    girl_mid: int
    skill_mid: int
    level: int
    polishing_count: int
    is_favorite: bool
    equipment_id: int
    pvp_equipment_id: int
    created_at: datetime
    updated_at: datetime | None


class GirlPotentialGetResponseModel(ModelBase):
    girl_potential_list: list[GirlPotentialModel]
