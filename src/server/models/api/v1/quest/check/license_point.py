from pydantic import BaseModel
from pydantic import ConfigDict


class QuestCheckLicensePointRequestModel(BaseModel):
    is_adjust: bool

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [{"is_adjust": False}],
        }
    )


class QuestCheckLicensePointResponseModel(BaseModel):
    # TODO

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [[]],
        }
    )
