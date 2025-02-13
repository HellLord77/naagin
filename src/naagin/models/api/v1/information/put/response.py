from naagin.bases import ModelBase


class InformationMarkAsReadModel(ModelBase):
    information_id: int


class InformationPutResponseModel(ModelBase):
    information_mark_as_read: InformationMarkAsReadModel
