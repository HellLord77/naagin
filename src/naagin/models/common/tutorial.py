from datetime import datetime

from naagin.bases import ModelBase


class TutorialModel(ModelBase):
    owner_id: int
    event_mid: int
    flag: int
    created_at: datetime
    updated_at: datetime | None
