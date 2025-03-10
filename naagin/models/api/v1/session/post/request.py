from naagin.bases import ModelBase


class SessionPostRequestModel(ModelBase):
    client_type: int
    environment: str | None = None
    is_first: int | None = None
    oauth_token: str
    oauth_token_secret: str
    onetime_token: str
    platform_id: int
