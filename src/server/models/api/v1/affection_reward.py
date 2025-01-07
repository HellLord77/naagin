from pydantic import BaseModel
from pydantic import ConfigDict


class AffectionRewardResponseModel(BaseModel):
    affection_level_reward_list: list  # TODO

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [{"affection_level_reward_list": []}],
        }
    )
