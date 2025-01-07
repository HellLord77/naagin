from pydantic import BaseModel
from pydantic import ConfigDict


class CasinoGameGetResponseModel(BaseModel):
    casino_game_list: list  # TODO

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [{"casino_game_list": []}],
        }
    )
