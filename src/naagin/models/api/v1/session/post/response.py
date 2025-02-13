from naagin.models.base import CustomBaseModel


class SessionPostResponseModel(CustomBaseModel):
    auth: bool
    owner_id: int
    owner_status: int
