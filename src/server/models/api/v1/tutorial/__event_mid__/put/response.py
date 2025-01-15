from datetime import datetime
from typing import Optional

from ...... import NaaginBaseModel


class OwnerModel(NaaginBaseModel):
    owner_id: int
    status: int
    name: str
    island_name: str
    message: str
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
    birthday: None
    stamina_checked_at: datetime
    last_logged_at: datetime
    friend_code: str
    created_at: datetime


class TutorialModel(NaaginBaseModel):
    owner_id: int
    event_mid: int
    flag: int
    created_at: datetime
    updated_at: Optional[datetime] = None


class TutorialEventMidPutResponseModel(NaaginBaseModel):
    owner_list: Optional[list[OwnerModel]] = None
    tutorial_list: list[TutorialModel]
