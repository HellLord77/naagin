from naagin.models.base import CustomBaseModel


class OptionItemAutoLockPostRequestModel(CustomBaseModel):
    option_lock_only: int
    option_lock_sr: int
    option_lock_ssr: int
