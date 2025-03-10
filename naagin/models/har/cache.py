from naagin.bases import HARModelBase

from .after_request import AfterRequestHARModel
from .before_request import BeforeRequestHARModel


class CacheHARModel(HARModelBase):
    before_request: BeforeRequestHARModel | None = None
    after_request: AfterRequestHARModel | None = None
