from pydantic import BaseModel
from pydantic import ConfigDict


class CasinoModifyDateGetResponseModel(BaseModel):
    casino_modify_date_list: list  # TODO

    model_config = ConfigDict(
        json_schema_extra={"examples": [{"casino_modify_date_list": []}]}
    )
