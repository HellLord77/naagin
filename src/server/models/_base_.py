from pydantic import BaseModel
from pydantic import ConfigDict


class NaaginBaseModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
