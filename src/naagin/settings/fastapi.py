from gzip import _COMPRESS_LEVEL_BEST
from zlib import Z_DEFAULT_COMPRESSION

from pydantic import NonNegativeInt
from pydantic_settings import SettingsConfigDict

from naagin.bases import SettingsBase
from naagin.types.fields import GZipCompressLevelField
from naagin.types.fields import ZLibCompressLevelField


class FastAPISettings(SettingsBase):
    swagger: bool = False

    limit: bool = True
    limit_max_size: NonNegativeInt = 1000

    gzip: bool = True
    gzip_min_size: NonNegativeInt = 500
    gzip_compress_level: GZipCompressLevelField = _COMPRESS_LEVEL_BEST

    deflate: bool = False
    deflate_min_size: NonNegativeInt = 500
    deflate_compress_level: ZLibCompressLevelField = Z_DEFAULT_COMPRESSION

    model_config = SettingsConfigDict(env_prefix="app_")
