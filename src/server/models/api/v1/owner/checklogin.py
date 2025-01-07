from pydantic import BaseModel
from pydantic import ConfigDict


class OwnerCheckLoginGetResponseModel(BaseModel):
    restart_required: bool

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [{"restart_required": False}],
        }
    )
