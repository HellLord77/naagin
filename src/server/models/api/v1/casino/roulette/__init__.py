from pydantic import BaseModel
from pydantic import ConfigDict


class CasinoRouletteResponseModel(BaseModel):
    roulette_info_list: list  # TODO

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [{"roulette_info_list": []}],
        }
    )
