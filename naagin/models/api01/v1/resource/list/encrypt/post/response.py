from naagin.bases import ModelBase
from naagin.types_.fields import MD5Field


class ResourceListEncryptPostResponseModel(ModelBase):
    resource_list_encrypt: str
    p: MD5Field
