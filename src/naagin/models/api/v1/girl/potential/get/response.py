from datetime import datetime
from typing import Optional

from naagin.models.base import BaseModel


class GirlPotentialModel(BaseModel):
    owner_id: int
    girl_mid: int
    skill_mid: int
    level: int
    polishing_count: int
    is_favorite: bool
    equipment_id: int
    pvp_equipment_id: int
    created_at: datetime
    updated_at: Optional[datetime]


class GirlPotentialGetResponseModel(BaseModel):
    girl_potential_list: list[GirlPotentialModel]
