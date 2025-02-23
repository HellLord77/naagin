from datetime import datetime

from pydantic import BaseModel  # noqa: TID251
from pydantic import ConfigDict
from pydantic.alias_generators import to_camel


class HARModelBase(BaseModel):
    comment: str | None = None

    model_config = ConfigDict(
        alias_generator=to_camel, json_encoders={datetime: lambda value: value.strftime("%Y-%m-%dT%H:%M:%SZ")}
    )
