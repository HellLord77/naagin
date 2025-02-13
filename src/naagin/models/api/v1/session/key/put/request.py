from naagin.models.base import CustomBaseModel


class SessionKeyPutRequestModel(CustomBaseModel):
    encrypt_key: str
