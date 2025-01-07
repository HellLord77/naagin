from pydantic import BaseModel
from pydantic import ConfigDict


class GiftboxCountGetResponseModel(BaseModel):
    giftbox_received_count: int

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [{"giftbox_received_count": 0}],
        }
    )
