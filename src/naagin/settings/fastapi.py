from gzip import _COMPRESS_LEVEL_BEST

from pydantic import NonNegativeInt
from pydantic_settings import SettingsConfigDict

from naagin.bases import SettingsBase
from naagin.types.fields import GZipCompressLevelField


class FastAPISettings(SettingsBase):
    process_time: bool = False
    swagger: bool = False

    limit: bool = True
    limit_max_size: NonNegativeInt = 1000

    gzip: bool = True
    gzip_min_size: NonNegativeInt = 500
    gzip_compress_level: GZipCompressLevelField = _COMPRESS_LEVEL_BEST

    model_config = SettingsConfigDict(env_prefix="app_")
