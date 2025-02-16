from typing import Protocol


class SupportsFlushEx(Protocol):
    def flush(self, data: bytes = b"") -> bytes: ...
