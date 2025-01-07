from pydantic import BaseModel
from pydantic import ConfigDict


class ItemConsumeNegativeResponseModel(BaseModel):
    item_negative_consume_list: list  # TODO

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [{"item_negative_consume_list": []}],
        }
    )
