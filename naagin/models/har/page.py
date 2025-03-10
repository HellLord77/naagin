from datetime import datetime

from naagin.bases import HARModelBase

from .page_timings import PageTimingsHARModel


class PageHARModel(HARModelBase):
    started_date_time: datetime
    id: str
    title: str
    page_timings: PageTimingsHARModel
