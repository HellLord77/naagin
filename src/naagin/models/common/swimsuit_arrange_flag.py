from datetime import datetime

from naagin.bases import ModelBase


class SwimsuitArrangeFlagModel(ModelBase):
    owner_id: int
    girl_mid: int
    variation: int
    switch: int
    created_at: datetime
    updated_at: datetime | None
