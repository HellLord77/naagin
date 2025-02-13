from datetime import datetime

from naagin.bases import ModelBase


class InformationModel(ModelBase):
    information_id: int
    title: str
    description: str
    html_page_url: str
    category: int
    publish_at: datetime
    close_at: datetime
    announce_at: None
    read: bool
    prohibit_popup: bool
    priority: int


class InformationGlobalPostResponseModel(ModelBase):
    information_list: list[InformationModel]
