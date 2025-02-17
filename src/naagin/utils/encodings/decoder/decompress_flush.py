from naagin.abstract import BaseDecoder
from naagin.proto import SupportsDecompressFlush


class DecompressFlushDecoder(BaseDecoder):
    def __init__(self, decompress_flush: SupportsDecompressFlush) -> None:
        self.decompress_flush = decompress_flush

    def update(self, data: bytes) -> bytes:
        return self.decompress_flush.decompress(data)

    def flush(self) -> bytes:
        return self.decompress_flush.flush()
