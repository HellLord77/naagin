from .common import SupportsCompress
from .common import SupportsFlush


class SupportsCompressFlush(SupportsCompress, SupportsFlush):
    pass
