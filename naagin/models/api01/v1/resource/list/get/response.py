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
    low: list[ResourceModel]
    common: list[ResourceModel]
    high: list[ResourceModel]
    exe: list[ResourceModel]


class ResourceListGetResponseModel(ModelBase):
    resource_list: ResourceListModel
