from naagin.bases import ModelBase


class OwnerPutRequestModel(ModelBase):
    name: str | None = None
    island_name: str | None = None
    message: str | None = None
