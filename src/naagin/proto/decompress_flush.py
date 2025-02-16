from .common import SupportsDecompress
from .common import SupportsFlush


class SupportsDecompressFlush(SupportsDecompress, SupportsFlush):
    pass
