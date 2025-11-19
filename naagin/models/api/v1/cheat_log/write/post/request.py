from naagin.bases import ModelBase


class CheatLogWritePostRequestModel(ModelBase):
    cheat_type: int
    owner_id: int
    param1: int
    param2: int
