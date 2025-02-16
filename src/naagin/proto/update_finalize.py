from .common import SupportsFinalize
from .common import SupportsUpdate


class SupportsUpdateFinalize(SupportsUpdate, SupportsFinalize):
    pass
