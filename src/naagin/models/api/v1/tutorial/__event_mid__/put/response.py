from naagin.bases import ModelBase
from naagin.models import OwnerOtherModel
from naagin.models import TutorialModel


class TutorialEventMidPutResponseModel(ModelBase):
    owner_list: list[OwnerOtherModel] | None = None
    tutorial_list: list[TutorialModel]
