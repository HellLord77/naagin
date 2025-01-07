from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class QuestActiveGetResponseModel(BaseModel):
    quest_active: Optional  # TODO

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [{"quest_active": None}],
        }
    )
