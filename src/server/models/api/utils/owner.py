from datetime import date
from datetime import datetime
from typing import Optional

from ...base import NaaginBaseModel


class OwnerModel(NaaginBaseModel):
    owner_id: int
    status: int
    name: Optional[str]
    island_name: Optional[str]
    message: Optional[str]
    team_id: int
    honor1_mid: int
    honor2_mid: int
    level: int
    experience: int
    stamina: int
    main_girl_mid: int
    lend_girl_mid: int
    spot_mid: int
    spot_phase_mid: int
    license_point: int
    license_level: int
    checked_license_level: int
    birthday: Optional[date]
    stamina_checked_at: datetime
    last_logged_at: datetime
    friend_code: str
    created_at: datetime
