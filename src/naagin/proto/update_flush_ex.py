from .common import SupportsFlushEx
from .common import SupportsUpdate


class SupportsUpdateFlushEx(SupportsUpdate, SupportsFlushEx):
    pass
