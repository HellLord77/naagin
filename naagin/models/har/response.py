from naagin.bases import HARModelBase

from .content import ContentHARModel
from .cookie import CookieHARModel
from .header import HeaderHARModel


class ResponseHARModel(HARModelBase):
    status: int
    status_text: str
    http_version: str
    cookies: list[CookieHARModel]
    headers: list[HeaderHARModel]
    content: ContentHARModel
    redirect_url: str
    headers_size: int = -1
    body_size: int = -1
