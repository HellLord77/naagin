from pydantic import BaseModel
from pydantic import ConfigDict


class MaintenancePrivilegeCheckResponseModel(BaseModel):
    result: str

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [{"result": "NG"}],
        },
    )
