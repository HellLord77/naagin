from datetime import datetime
from typing import Optional

from .....other_owner import OtherOwnerModel
from ......base import NaaginBaseModel


class TutorialModel(NaaginBaseModel):
    owner_id: int
    event_mid: int
    flag: int
    created_at: datetime
    updated_at: Optional[datetime]


class TutorialEventMidPutResponseModel(NaaginBaseModel):
    owner_list: Optional[list[OtherOwnerModel]] = None
    tutorial_list: list[TutorialModel]
