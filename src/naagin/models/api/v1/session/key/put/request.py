from naagin.models.base import BaseModel


class SessionKeyPutRequestModel(BaseModel):
    encrypt_key: str
