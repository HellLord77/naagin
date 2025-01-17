from datetime import datetime
from typing import Optional

from naagin.models.base import BaseModel
from naagin.models.utils import OtherOwnerModel


class TutorialModel(BaseModel):
    owner_id: int
    event_mid: int
    flag: int
    created_at: datetime
    updated_at: Optional[datetime]


class TutorialEventMidPutResponseModel(BaseModel):
    owner_list: Optional[list[OtherOwnerModel]] = None
    tutorial_list: list[TutorialModel]
