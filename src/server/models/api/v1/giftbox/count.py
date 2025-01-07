from pydantic import BaseModel
from pydantic import ConfigDict


class GiftboxCountResponseModel(BaseModel):
    giftbox_received_count: int

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [{"giftbox_received_count": 0}],
        }
    )
