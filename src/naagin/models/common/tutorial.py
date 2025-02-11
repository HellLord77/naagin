from datetime import datetime

from naagin.models.base import BaseModel


class TutorialModel(BaseModel):
    owner_id: int
    event_mid: int
    flag: int
    created_at: datetime
    updated_at: datetime | None
