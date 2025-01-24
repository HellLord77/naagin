from cryptography.hazmat.primitives.padding import PaddingContext

from .base import BaseEncoder


class PaddingEncoder(BaseEncoder):
    def __init__(self, padder: PaddingContext):
        self.padder = padder

    def update(self, data: bytes) -> bytes:
        return self.padder.update(data)

    def flush(self, data: bytes = b"") -> bytes:
        if data:
            data = self.padder.update(data)
        return data + self.padder.finalize()
