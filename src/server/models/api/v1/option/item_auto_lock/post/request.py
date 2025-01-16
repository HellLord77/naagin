from ......base import NaaginBaseModel


class OptionItemAutoLockPostRequestModel(NaaginBaseModel):
    option_lock_only: int
    option_lock_sr: int
    option_lock_ssr: int
