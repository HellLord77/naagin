from naagin.models.base import CustomBaseModel


class JohrenAuthJohrenOnetimeTokenGetResponse(CustomBaseModel):
    oauth_token_secret: str
