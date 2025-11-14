from naagin.bases import ModelBase
from naagin.types_.fields import MD5Field


class ResourceKeyPlatformIdGetResponseModel(ModelBase):
    e: str
    p: MD5Field
