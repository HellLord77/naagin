from naagin.bases import ModelBase


class GuestModel(ModelBase):
    guest_id: int
    state: int
    group: str
    rank: int
    guest_point: int
    cover_girl_bonus_rate_list: list


class QuestGuestListGetResponseModel(ModelBase):
    guest_list: list[GuestModel]
