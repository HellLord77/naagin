from typing import Annotated
from typing import Literal

from pydantic import Field
from pydantic import PositiveInt

from naagin import settings
from naagin.bases import ModelBase
from naagin.types.fields import EXEField
from naagin.types.fields import MD5Field


class ResourceModel(ModelBase):
    version: Annotated[int, Field(le=settings.version.application)]
    directory: Literal[""]
    file_name: EXEField
    file_size: PositiveInt
    hash: MD5Field


class ResourceListModel(ModelBase):
    low: list[ResourceModel]
    common: list[ResourceModel]
    high: list[ResourceModel]
    exe: list[ResourceModel]


class ResourceListGetResponseModel(ModelBase):
    resource_list: ResourceListModel
