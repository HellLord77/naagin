from datetime import datetime
from typing import Optional

from ..... import NaaginBaseModel


class TutorialModel(NaaginBaseModel):
    owner_id: int
    event_mid: int
    flag: int
    created_at: datetime
    updated_at: Optional[datetime]


class TutorialGetResponseModel(NaaginBaseModel):
    tutorial_list: list[TutorialModel]
