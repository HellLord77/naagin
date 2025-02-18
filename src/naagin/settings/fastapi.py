from zlib import Z_BEST_COMPRESSION

from pydantic import NonNegativeInt
from pydantic_settings import SettingsConfigDict

from naagin.bases import SettingsBase
from naagin.types.fields import ZLibCompressLevelField


class FastAPISettings(SettingsBase):
    swagger: bool = False

    limit: bool = True
    limit_max_size: NonNegativeInt = 1000

    gzip: bool = True
    gzip_min_size: NonNegativeInt = 500
    gzip_compress_level: ZLibCompressLevelField = Z_BEST_COMPRESSION

    model_config = SettingsConfigDict(env_prefix="app_")
