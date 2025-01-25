from zlib import compressobj

from naagin import settings
from .base import BaseEncoder


class DeflateEncoder(BaseEncoder):
    def __init__(self):
        self.compressobj = compressobj(settings.api.compress_level)

    def update(self, data: bytes) -> bytes:
        return self.compressobj.compress(data)

    def flush(self, data: bytes = b"") -> bytes:
        if data:
            data = self.compressobj.compress(data)
        return data + self.compressobj.flush()
