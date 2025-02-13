from naagin.models.base import CustomBaseModel


class ExceptionModel(CustomBaseModel):
    code: int
    message: str
