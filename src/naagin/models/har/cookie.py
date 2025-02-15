from datetime import datetime

from naagin.bases import HARModelBase


class CookieHARModel(HARModelBase):
    name: str
    value: str
    path: str | None = None
    domain: str | None = None
    expires: datetime | None = None
    http_only: bool | None = None
    secure: bool | None = None
