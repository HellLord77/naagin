from pydantic import BaseModel
from pydantic import ConfigDict


class SubscriptionModel(BaseModel):
    owner_fp: list[int]
    pass_details: list  # TODO


class SubscriptionGetResponseModel(BaseModel):
    subscription_list: SubscriptionModel

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {"subscription_list": {"owner_fp": [0, 0], "pass_details": []}}
            ],
        }
    )
