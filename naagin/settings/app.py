from gzip import _COMPRESS_LEVEL_BEST
from typing import Annotated

from pydantic import AliasChoices
from pydantic import Field
from pydantic import NonNegativeInt

from naagin.bases import SettingsBase
from naagin.types_.fields import GZipCompressLevelField


class AppSettings(SettingsBase):
    swagger_ui: Annotated[bool, Field(validation_alias=AliasChoices("swagger_ui", "swagger"))] = False
    debug_headers: Annotated[bool, Field(validation_alias=AliasChoices("debug_headers", "debug"))] = False

    limit_request: Annotated[bool, Field(validation_alias=AliasChoices("limit_request", "limit"))] = True
    limit_maximum_size: Annotated[
        NonNegativeInt, Field(validation_alias=AliasChoices("limit_maximum_size", "limit_max_size"))
    ] = 1000

    gzip_response: Annotated[bool, Field(validation_alias=AliasChoices("gzip_response", "gzip"))] = True
    gzip_minimum_size: Annotated[
        NonNegativeInt, Field(validation_alias=AliasChoices("gzip_minimum_size", "gzip_min_size"))
    ] = 500
    gzip_compress_level: GZipCompressLevelField = _COMPRESS_LEVEL_BEST
