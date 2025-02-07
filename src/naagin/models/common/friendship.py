from datetime import datetime

from naagin.models.base import BaseModel


class FriendshipModel(BaseModel):
    owner_id: int
    friend_id: int
    state: int
    invited: bool
    sent_at: datetime
    created_at: datetime
    updated_at: datetime | None
