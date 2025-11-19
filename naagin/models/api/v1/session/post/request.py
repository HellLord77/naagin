from naagin.bases import ModelBase


class SessionPostRequestModel(ModelBase):
    client_type: int | None = None
    environment: str | None = None
    is_first: int | None = None
    oauth_token: str | None = None
    oauth_token_secret: str | None = None
    onetime_token: str
    platform_id: int
