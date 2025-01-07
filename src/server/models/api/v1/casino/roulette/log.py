from pydantic import BaseModel
from pydantic import ConfigDict


class CasinoRouletteLogResponseModel(BaseModel):
    roulette_log_list: list  # TODO

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [{"roulette_log_list": []}],
        }
    )
