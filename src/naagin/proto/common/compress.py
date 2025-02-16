from typing import Protocol


class SupportsCompress(Protocol):
    def compress(self, data: bytes) -> bytes: ...
