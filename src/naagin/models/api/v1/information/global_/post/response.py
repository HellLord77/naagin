from datetime import datetime

from naagin.models.base import BaseModel


class InformationModel(BaseModel):
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


class InformationGlobalPostResponseModel(BaseModel):
    information_list: list[InformationModel]
