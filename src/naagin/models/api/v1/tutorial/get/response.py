from naagin.models.base import BaseModel
from naagin.models.common import TutorialModel


class TutorialGetResponseModel(BaseModel):
    tutorial_list: list[TutorialModel]
