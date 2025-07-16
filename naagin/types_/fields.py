from gzip import _COMPRESS_LEVEL_BEST
from gzip import _COMPRESS_LEVEL_FAST
from typing import Annotated
from zlib import Z_BEST_COMPRESSION
from zlib import Z_DEFAULT_COMPRESSION

from pydantic import Field

PortField = Annotated[int, Field(ge=0, le=65535)]
ZLibCompressLevelField = Annotated[int, Field(ge=Z_DEFAULT_COMPRESSION, le=Z_BEST_COMPRESSION)]
GZipCompressLevelField = Annotated[int, Field(ge=_COMPRESS_LEVEL_FAST - 1, le=_COMPRESS_LEVEL_BEST)]

MD5Field = Annotated[str, Field(pattern=r"^[a-f\d]{32}$")]
CSVField = Annotated[str, Field(pattern=r"^[a-zA-Z_]+\.csv$")]
EXEField = Annotated[str, Field(pattern=r"^\w+\.exe$")]
