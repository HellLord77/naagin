from datetime import datetime

from naagin.models.base import BaseModel
from naagin.models.common import OwnerOtherModel


class TutorialModel(BaseModel):
    owner_id: int
    event_mid: int
    flag: int
    created_at: datetime
    updated_at: datetime | None


class TutorialEventMidPutResponseModel(BaseModel):
    owner_list: list[OwnerOtherModel] | None = None
    tutorial_list: list[TutorialModel]
