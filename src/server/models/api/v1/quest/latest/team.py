from pydantic import BaseModel
from pydantic import ConfigDict


class QuestLatestTeamModel(BaseModel):
    owner_id: int
    quest_mid: int
    girl_mid_forward: int
    girl_mid_back: int
    girl_mid_substitute: int


class QuestLatestTeamResponseModel(BaseModel):
    quest_latest_team: QuestLatestTeamModel

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "quest_latest_team": {
                        "owner_id": 288696,
                        "quest_mid": 32559001,
                        "girl_mid_forward": 12,
                        "girl_mid_back": 16,
                        "girl_mid_substitute": -1,
                    }
                }
            ],
        }
    )
