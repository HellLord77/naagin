from naagin.bases import ModelBase


class AffectionLevelRewardModel(ModelBase):
    content_mid: int
    girl_mid: int
    accepted_level: int


class AffectionRewardGetResponseModel(ModelBase):
    affection_level_reward_list: list[AffectionLevelRewardModel]
