from pydantic import BaseModel
from pydantic import ConfigDict


class GamestartGetResponseModel(BaseModel):
    gamestart: bool

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [{"gamestart": True}],
        },
    )
