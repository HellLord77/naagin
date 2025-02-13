from naagin.models.base import CustomBaseModel


class SessionKeyGetResponseModel(CustomBaseModel):
    encrypt_key: str
