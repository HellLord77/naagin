from naagin.bases import HARModelBase


class ContentHARModel(HARModelBase):
    size: int
    compression: int | None = None
    mime_type: str
    text: str | None = None
    encoding: str | None = None
