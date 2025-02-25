from gzip import _COMPRESS_LEVEL_BEST

from pydantic import NonNegativeInt
from pydantic_settings import SettingsConfigDict

from naagin.bases import SettingsBase
from naagin.types.fields import GZipCompressLevelField


class AppSettings(SettingsBase):
    swagger_ui: bool = False
    debug_headers: bool = False
    _user_agent: str = "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko"

    limit: bool = True
    limit_max_size: NonNegativeInt = 1000

    gzip: bool = True
    gzip_min_size: NonNegativeInt = 500
    gzip_compress_level: GZipCompressLevelField = _COMPRESS_LEVEL_BEST

    model_config = SettingsConfigDict(env_prefix="app_")
