from naagin.models.base import BaseModel


class SessionKeyGetResponseModel(BaseModel):
    encrypt_key: str
