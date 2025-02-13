from naagin.bases import ModelBase


class OptionItemAutoLockPostRequestModel(ModelBase):
    option_lock_only: int
    option_lock_sr: int
    option_lock_ssr: int
