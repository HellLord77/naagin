from pydantic import BaseModel
from pydantic import ConfigDict


class FriendshipResponseModel(BaseModel):
    friendship_list: list  # TODO

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [{"friendship_list": []}],
        }
    )
