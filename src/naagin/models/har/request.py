from naagin.bases import HARModelBase

from .cookie import CookieHARModel
from .header import HeaderHARModel
from .post_data import PostDataHARModel
from .query_string import QueryStringHARModel


class RequestHARModel(HARModelBase):
    method: str
    url: str
    http_version: str
    cookies: list[CookieHARModel]
    headers: list[HeaderHARModel]
    query_string: list[QueryStringHARModel]
    post_data: PostDataHARModel | None = None
    headers_size: int = -1
    body_size: int = -1
