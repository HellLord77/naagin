from pydantic import BaseModel
from pydantic import ConfigDict


class LoginBonusSharedCheckGetResponseModel(BaseModel):
    login_bonus_shared_bonus_id_list: list  # TODO

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [{"login_bonus_shared_bonus_id_list": []}],
        }
    )
