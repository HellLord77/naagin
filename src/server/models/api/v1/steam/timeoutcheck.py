from pydantic import BaseModel
from pydantic import ConfigDict


class SteamTimeoutCheckResponseModel(BaseModel):
    steam_timeout_check_result: bool

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [{"steam_timeout_check_result": False}],
        }
    )
