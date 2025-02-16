from typing import Protocol


class SupportsUpdate(Protocol):
    def update(self, data: bytes) -> bytes: ...
