from naagin.models.base import BaseModel


class SessionPostResponseModel(BaseModel):
    auth: bool
    owner_id: int
    owner_status: int
