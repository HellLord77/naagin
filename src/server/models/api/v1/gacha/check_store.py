from pydantic import BaseModel
from pydantic import ConfigDict


class GachaCheckStoreResponseModel(BaseModel):
    # TODO

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [[]],
        }
    )
