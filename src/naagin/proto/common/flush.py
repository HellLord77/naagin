from typing import Protocol


class SupportsFlush(Protocol):
    def flush(self) -> bytes: ...
