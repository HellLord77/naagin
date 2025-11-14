from naagin.bases import ModelBase


class SteamJaSessionPostRequestModel(ModelBase):
    environment: str | None = None
    is_first: int | None = None
    onetime_token: str
    platform_id: str
