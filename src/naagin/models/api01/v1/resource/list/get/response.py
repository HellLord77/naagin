from naagin.bases import ModelBase


class ResourceModel(ModelBase):
    version: int
    directory: str
    file_name: str
    file_size: int
    hash: str


class ResourceListModel(ModelBase):
    low: list[ResourceModel]
    common: list[ResourceModel]
    high: list[ResourceModel]
    exe: list[ResourceModel]


class ResourceListGetResponseModel(ModelBase):
    resource_list: ResourceListModel
