from pydantic import BaseModel
from pydantic import ConfigDict


class CheatLogCheckGetResponseModel(BaseModel):
    count: int

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [{"count": 0}],
        }
    )
