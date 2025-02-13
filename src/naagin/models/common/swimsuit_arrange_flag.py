from datetime import datetime

from naagin.models.base import CustomBaseModel


class SwimsuitArrangeFlagModel(CustomBaseModel):
    owner_id: int
    girl_mid: int
    variation: int
    switch: int
    created_at: datetime
    updated_at: datetime | None
