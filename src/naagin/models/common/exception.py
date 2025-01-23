from naagin.models.base import BaseModel


class ExceptionModel(BaseModel):
    code: int
    message: str
