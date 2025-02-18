from typing import Annotated
from zlib import Z_BEST_SPEED

from pydantic_settings import SettingsConfigDict

from naagin.bases import SettingsBase
from naagin.types.fields import ZLibCompressLevelField


class APISettings(SettingsBase):
    compress: bool = True
    compress_level: Annotated[int, ZLibCompressLevelField] = Z_BEST_SPEED

    encrypt: bool = True

    model_config = SettingsConfigDict(env_prefix="api_")
