from naagin.abstract import BaseEncoding
from naagin.proto import SupportsUpdateFlush


class MultiEncoding(BaseEncoding):
    def __init__(self, *encodings: SupportsUpdateFlush) -> None:
        self.encodings = encodings

    def update(self, data: bytes) -> bytes:
        for encoding in self.encodings:
            data = encoding.update(data)
        return data

    def flush(self) -> bytes:
        data = b""
        for encoding in self.encodings:
            data = encoding.update(data) + encoding.flush()
        return data
