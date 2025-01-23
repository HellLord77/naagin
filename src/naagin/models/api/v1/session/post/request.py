from typing import Optional

from naagin.models.base import BaseModel


class SessionPostRequestModel(BaseModel):
    client_type: int
    environment: Optional[str] = None
    is_first: Optional[int] = None
    oauth_token: str
    oauth_token_secret: str
    onetime_token: str
    platform_id: int
