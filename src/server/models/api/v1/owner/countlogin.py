from pydantic import BaseModel
from pydantic import ConfigDict


class OwnerCountLoginResponseModel(BaseModel):
    login_count: int

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [{"login_count": 38}],
        }
    )
