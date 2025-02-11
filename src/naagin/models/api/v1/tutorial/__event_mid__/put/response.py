from naagin.models.base import BaseModel
from naagin.models.common import OwnerOtherModel
from naagin.models.common import TutorialModel


class TutorialEventMidPutResponseModel(BaseModel):
    owner_list: list[OwnerOtherModel] | None = None
    tutorial_list: list[TutorialModel]
