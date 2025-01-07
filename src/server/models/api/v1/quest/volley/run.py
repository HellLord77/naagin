from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class QuestRunModel(BaseModel):
    owner_id: int
    gold_ball_used_at: Optional  # TODO
    challenge_fes_started_at: Optional  # TODO
    collect_fes_number: int


class QuestVolleyRunResponseModel(BaseModel):
    quest_run: QuestRunModel

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "quest_run": {
                        "owner_id": 288696,
                        "gold_ball_used_at": None,
                        "challenge_fes_started_at": None,
                        "collect_fes_number": 153,
                    }
                }
            ],
        }
    )
