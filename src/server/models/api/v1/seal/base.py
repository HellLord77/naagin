from pydantic import BaseModel
from pydantic import ConfigDict


class SealBaseModel(BaseModel):
    girl_mid: int
    main_base_mid: int
    sub_base_mid: int


class SealBaseResponseModel(BaseModel):
    seal_base_list: list[SealBaseModel]

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "seal_base_list": [
                        {"girl_mid": 3, "main_base_mid": 2, "sub_base_mid": 18},
                        {"girl_mid": 7, "main_base_mid": 6, "sub_base_mid": 22},
                        {"girl_mid": 11, "main_base_mid": 10, "sub_base_mid": 26},
                        {"girl_mid": 16, "main_base_mid": 15, "sub_base_mid": 31},
                    ]
                }
            ],
        }
    )
