from naagin.models.base import CustomBaseModel


class ResourceModel(CustomBaseModel):
    version: int
    directory: str
    file_name: str
    file_size: int
    hash: str


class ResourceListModel(CustomBaseModel):
    low: list[ResourceModel]
    common: list[ResourceModel]
    high: list[ResourceModel]
    exe: list[ResourceModel]


class ResourceListGetResponseModel(CustomBaseModel):
    resource_list: ResourceListModel
