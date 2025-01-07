from pydantic import BaseModel
from pydantic import ConfigDict


class OptionItemAutoLockRequestModel(BaseModel):
    option_lock_only: int
    option_lock_sr: int
    option_lock_ssr: int

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {"option_lock_only": 1, "option_lock_sr": 1, "option_lock_ssr": 1}
            ],
        }
    )


class OptionItemAutoLockResponseModel(BaseModel):
    # TODO

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [[]],
        }
    )
