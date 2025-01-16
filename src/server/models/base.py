from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class NaaginBaseModel(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_encoders={datetime: lambda value: value.strftime("%Y-%m-%d %H:%M:%S")},
    )
