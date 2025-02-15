from naagin.bases import HARModelBase


class PageTimingsHARModel(HARModelBase):
    on_content_load: float | None = -1
    on_load: float | None = -1
