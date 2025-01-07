from pydantic import BaseModel
from pydantic import ConfigDict


class BgmModel(BaseModel):
    scene_mid: int
    list_index: int
    bgm_mid: int


class RadioStationBgmGetResponseModel(BaseModel):
    bgm_list: list[BgmModel]

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {"bgm_list": [{"scene_mid": 0, "list_index": 0, "bgm_mid": 0}]}
            ],
        }
    )
