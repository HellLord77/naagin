from naagin.models.base import CustomBaseModel


class OwnerPutRequestModel(CustomBaseModel):
    name: str | None = None
    island_name: str | None = None
    message: str | None = None
