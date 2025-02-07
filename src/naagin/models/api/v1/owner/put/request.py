from naagin.models.base import BaseModel


class OwnerPutRequestModel(BaseModel):
    name: str | None = None
    island_name: str | None = None
    message: str | None = None
