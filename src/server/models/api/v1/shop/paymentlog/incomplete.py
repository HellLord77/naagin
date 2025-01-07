from pydantic import BaseModel
from pydantic import ConfigDict


class ShopPaymentLogIncompleteResponseModel(BaseModel):
    payment_log_list: list  # TODO

    model_config = ConfigDict(
        json_schema_extra={"examples": [{"payment_log_list": []}]}
    )
