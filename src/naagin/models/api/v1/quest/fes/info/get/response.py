from naagin.models.base import CustomBaseModel


class QuestFesInfoGetResponseModel(CustomBaseModel):
    open_bonus_fes_list: list
    quest_daily_info_list: list
