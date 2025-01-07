from pydantic import BaseModel
from pydantic import ConfigDict


class GirlHeadAccessorySwitchListResponseModel(BaseModel):
    head_accessary_switch_list: list  # TODO

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [{"head_accessary_switch_list": []}],
        }
    )
