from pydantic import BaseModel
from pydantic import ConfigDict


class QuestCheckLicensePointPostRequestModel(BaseModel):
    is_adjust: bool

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [{"is_adjust": False}],
        }
    )


class QuestCheckLicensePointPostResponseModel(BaseModel):
    # TODO

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [[]],
        }
    )
