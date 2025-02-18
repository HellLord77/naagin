from naagin.bases import ModelBase


class ExceptionModel(ModelBase):
    code: int
    message: str
