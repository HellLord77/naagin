from naagin.models.base import CustomBaseModel


class InformationMarkAsReadModel(CustomBaseModel):
    information_id: int


class InformationPutResponseModel(CustomBaseModel):
    information_mark_as_read: InformationMarkAsReadModel
