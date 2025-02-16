from naagin.abstract import BaseEncoder
from naagin.proto import SupportsUpdateFinalize


class UpdateFinalizeEncoder(BaseEncoder):
    def __init__(self, update_finalize: SupportsUpdateFinalize) -> None:
        self.update_finalize = update_finalize

    def update(self, data: bytes) -> bytes:
        return self.update_finalize.update(data)

    def flush(self, data: bytes = b"") -> bytes:
        if data:
            data = self.update(data)
        return data + self.update_finalize.finalize()
