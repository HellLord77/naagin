from pydantic import BaseModel
from pydantic import ConfigDict


class VenusBoardStatusGetResponseModel(BaseModel):
    venus_board_status_list: list  # TODO

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [{"venus_board_status_list": []}],
        }
    )
