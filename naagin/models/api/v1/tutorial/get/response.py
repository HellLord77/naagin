from naagin.bases import ModelBase
from naagin.models import TutorialModel


class TutorialGetResponseModel(ModelBase):
    tutorial_list: list[TutorialModel]
