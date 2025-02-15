from datetime import datetime

from naagin.bases import HARModelBase


class AfterRequestHARModel(HARModelBase):
    expires: datetime | None = None
    last_access: datetime
    e_tag: str
    hit_count: int
