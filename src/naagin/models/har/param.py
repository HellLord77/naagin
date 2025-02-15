from naagin.bases import HARModelBase


class ParamHARModel(HARModelBase):
    name: str
    value: str | None = None
    file_name: str | None = None
    content_type: str | None = None
