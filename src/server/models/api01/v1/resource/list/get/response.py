from ......base import NaaginBaseModel


class ResourceModel(NaaginBaseModel):
    version: int
    directory: str
    file_name: str
    file_size: int
    hash: str


class ResourceListModel(NaaginBaseModel):
    low: list[ResourceModel]
    common: list[ResourceModel]
    high: list[ResourceModel]
    exe: list[ResourceModel]


class ResourceListGetResponseModel(NaaginBaseModel):
    resource_list: ResourceListModel
