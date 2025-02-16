from naagin.abstract import BaseEncoder
from naagin.proto import SupportsCompressFlush


class CompressFlushEncoder(BaseEncoder):
    def __init__(self, compress_flush: SupportsCompressFlush) -> None:
        self.compress_flush = compress_flush

    def update(self, data: bytes) -> bytes:
        return self.compress_flush.compress(data)

    def flush(self, data: bytes = b"") -> bytes:
        if data:
            data = self.update(data)
        return data + self.compress_flush.flush()
