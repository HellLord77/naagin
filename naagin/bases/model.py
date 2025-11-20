from datetime import datetime

from pydantic import BaseModel  # noqa: TID251
from pydantic import ConfigDict


class ModelBase(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        from_attributes=True,
        json_encoders={datetime: lambda value: value.strftime("%Y-%m-%d %H:%M:%S")},
    )
