from ......base import BaseModel


class OptionItemAutoLockPostRequestModel(BaseModel):
    option_lock_only: int
    option_lock_sr: int
    option_lock_ssr: int
