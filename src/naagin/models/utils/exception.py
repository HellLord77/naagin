from ..base import BaseModel


class ExceptionModel(BaseModel):
    code: int
    message: str
