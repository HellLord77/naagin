from naagin.bases import ModelBase


class SessionPostResponseModel(ModelBase):
    auth: bool
    owner_id: int
    owner_status: int
