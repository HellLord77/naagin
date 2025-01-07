from pydantic import BaseModel
from pydantic import ConfigDict


class GirlPrivateFavoriteResponseModel(BaseModel):
    favorite_private_item_list: list  # TODO

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [{"favorite_private_item_list": []}],
        }
    )
