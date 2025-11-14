from naagin.bases import ModelBase


class SteamJaSessionPostResponseModel(ModelBase):
    auth: bool
    owner_id: int
    owner_status: int
