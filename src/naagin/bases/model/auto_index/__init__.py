from datetime import datetime

from pydantic import BaseModel  # noqa: TID251
from pydantic import ConfigDict


class AutoIndexModelBase(BaseModel):
    model_config = ConfigDict(json_encoders={datetime: lambda value: value.strftime("%a, %d %b %Y %H:%M:%S GMT")})
