from pydantic import BaseModel
from pydantic import ConfigDict


class MaintenanceResponseModel(BaseModel):
    maintenance: bool

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [{"maintenance": False}],
        },
    )
