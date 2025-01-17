from naagin.models.base import BaseModel


class ResourceModel(BaseModel):
    version: int
    directory: str
    file_name: str
    file_size: int
    hash: str


class ResourceListModel(BaseModel):
    low: list[ResourceModel]
    common: list[ResourceModel]
    high: list[ResourceModel]
    exe: list[ResourceModel]


class ResourceListGetResponseModel(BaseModel):
    resource_list: ResourceListModel
