from typing import Annotated
from zlib import Z_BEST_COMPRESSION
from zlib import Z_DEFAULT_COMPRESSION

from pydantic import Field

PortField = Annotated[int, Field(ge=0, le=65535)]
ZLibCompressLevelField = Annotated[int, Field(ge=Z_DEFAULT_COMPRESSION, le=Z_BEST_COMPRESSION)]
