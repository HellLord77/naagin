from pydantic import BaseModel
from pydantic import ConfigDict


class DynamicGameParameterGetResponseModel(BaseModel):
    dynamic_game_parameter_list: list  # TODO

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [{"dynamic_game_parameter_list": []}],
        }
    )
