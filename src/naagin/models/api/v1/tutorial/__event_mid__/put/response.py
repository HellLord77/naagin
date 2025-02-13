from naagin.bases import ModelBase
from naagin.models.common import OwnerOtherModel
from naagin.models.common import TutorialModel


class TutorialEventMidPutResponseModel(ModelBase):
    owner_list: list[OwnerOtherModel] | None = None
    tutorial_list: list[TutorialModel]
