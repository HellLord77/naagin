from .common import SupportsFlush
from .common import SupportsUpdate


class SupportsUpdateFlush(SupportsUpdate, SupportsFlush):
    pass
