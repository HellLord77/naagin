from datetime import datetime

from naagin.bases import ModelBase


class QuestModel(ModelBase):
    quest_mid: int
    quest_new: bool
    quest_clear: bool
    clear_rank: int
    started_at: datetime
    first_cleared_at: datetime | None
    srank_cleared_at: datetime | None
    arank_cleared_at: datetime | None


class QuestListGetResponseModel(ModelBase):
    quest_list: list[QuestModel]
    auto_fes_attempts: int
