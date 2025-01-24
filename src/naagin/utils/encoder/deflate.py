from zlib import compressobj

from .base import BaseEncoder


class DeflateEncoder(BaseEncoder):
    def __init__(self):
        self.compressobj = compressobj()

    def update(self, data: bytes) -> bytes:
        return self.compressobj.compress(data)

    def flush(self, data: bytes = b"") -> bytes:
        if data:
            data = self.compressobj.compress(data)
        return data + self.compressobj.flush()
