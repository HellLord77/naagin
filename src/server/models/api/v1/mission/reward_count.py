from pydantic import BaseModel
from pydantic import ConfigDict


class MissionRewardCountGetResponseModel(BaseModel):
    mission_reward_count_list: list  # TODO

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [{"mission_reward_count_list": []}],
        }
    )
