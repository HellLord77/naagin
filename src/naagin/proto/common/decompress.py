from typing import Protocol


class SupportsDecompress(Protocol):
    def decompress(self, data: bytes) -> bytes: ...
