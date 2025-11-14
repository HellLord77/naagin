from naagin.bases import ModelBase
from naagin.types_.fields import SHA256Field


class ResourceListEncryptPostRequestModel(ModelBase):
    key: SHA256Field
    platform_id: int
