from pydantic import BaseModel
from pydantic import ConfigDict


class QuestFesInfoResponseModel(BaseModel):
    open_bonus_fes_list: list  # TODO
    quest_daily_info_list: list  # TODO

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [{"open_bonus_fes_list": [], "quest_daily_info_list": []}],
        }
    )
