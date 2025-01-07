from pydantic import BaseModel
from pydantic import ConfigDict


class OwnerCountLoginGetResponseModel(BaseModel):
    ranking_active_id_list: list[int]

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [{"ranking_active_id_list": [302, 354]}],
        }
    )
