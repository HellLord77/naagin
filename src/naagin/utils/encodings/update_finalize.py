from naagin.abstract import BaseEncoding
from naagin.proto import SupportsUpdateFinalize


class UpdateFinalizeEncoding(BaseEncoding):
    def __init__(self, update_finalize: SupportsUpdateFinalize) -> None:
        self.update_finalize = update_finalize

    def update(self, data: bytes) -> bytes:
        return self.update_finalize.update(data)

    def flush(self) -> bytes:
        return self.update_finalize.finalize()
