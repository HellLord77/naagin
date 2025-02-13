from naagin.models.base import CustomBaseModel
from naagin.models.common import OwnerOtherModel
from naagin.models.common import TutorialModel


class TutorialEventMidPutResponseModel(CustomBaseModel):
    owner_list: list[OwnerOtherModel] | None = None
    tutorial_list: list[TutorialModel]
