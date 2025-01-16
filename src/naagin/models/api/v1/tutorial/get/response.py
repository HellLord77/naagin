from datetime import datetime
from typing import Optional

from .....base import BaseModel


class TutorialModel(BaseModel):
    owner_id: int
    event_mid: int
    flag: int
    created_at: datetime
    updated_at: Optional[datetime]


class TutorialGetResponseModel(BaseModel):
    tutorial_list: list[TutorialModel]
