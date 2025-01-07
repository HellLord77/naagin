from pydantic import BaseModel
from pydantic import ConfigDict


class QuestStaminaGetResponseModel(BaseModel):
    quest_girl_stamina_list: list  # TODO

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [{"quest_girl_stamina_list": []}],
        }
    )
