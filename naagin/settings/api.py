from typing import Annotated
from zlib import Z_BEST_SPEED

from pydantic import AliasChoices
from pydantic import Field

from naagin.bases import SettingsBase
from naagin.types_.fields import ZLibCompressLevelField


class APISettings(SettingsBase):
    compress_enabled: Annotated[bool, Field(validation_alias=AliasChoices("compress_enabled", "compress"))] = True
    compress_level: ZLibCompressLevelField = Z_BEST_SPEED

    encrypt_enabled: Annotated[bool, Field(validation_alias=AliasChoices("encrypt_enabled", "encrypt"))] = True
