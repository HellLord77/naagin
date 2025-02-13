from naagin.models.base import CustomBaseModel
from naagin.models.common import TutorialModel


class TutorialGetResponseModel(CustomBaseModel):
    tutorial_list: list[TutorialModel]
