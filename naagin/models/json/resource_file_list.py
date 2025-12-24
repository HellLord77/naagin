from typing import Annotated

from pydantic import Field
from pydantic import PositiveInt

from naagin.bases import ModelBase
from naagin.types_.fields import EXEField
from naagin.types_.fields import MD5Field


class ResourceModel(ModelBase):
    version: int
    directory: str
    file_name: EXEField
    file_size: PositiveInt
    hash: MD5Field


class ResourceListModel(ModelBase):
    common: Annotated[list[ResourceModel], Field(min_length=1)]
    high: Annotated[list[ResourceModel], Field(min_length=1)]
    low: Annotated[list[ResourceModel], Field(min_length=1)]
    exe: Annotated[list[ResourceModel], Field(min_length=1, max_length=1)]


class ResourceFileListModel(ModelBase):
    resource_list: ResourceListModel
