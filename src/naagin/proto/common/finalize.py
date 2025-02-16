from typing import Protocol


class SupportsFinalize(Protocol):
    def finalize(self) -> bytes: ...
