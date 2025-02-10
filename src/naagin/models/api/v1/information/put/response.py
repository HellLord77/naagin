from naagin.models.base import BaseModel


class InformationMarkAsReadModel(BaseModel):
    information_id: int


class InformationPutResponseModel(BaseModel):
    information_mark_as_read: InformationMarkAsReadModel
