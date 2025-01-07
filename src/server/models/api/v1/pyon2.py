from pydantic import BaseModel
from pydantic import ConfigDict


class Pyon2RunModel(BaseModel):
    owner_id: int
    girl_mid: int
    stage_mid: int
    lane_id: int
    pos_id: int


class Pyon2GetResponseModel(BaseModel):
    pyon2_run_list: list[Pyon2RunModel]

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "pyon2_run_list": [
                        {
                            "owner_id": 288696,
                            "girl_mid": 0,
                            "stage_mid": 0,
                            "lane_id": 0,
                            "pos_id": 0,
                        }
                    ]
                }
            ],
        }
    )
