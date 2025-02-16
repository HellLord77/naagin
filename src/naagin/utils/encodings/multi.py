from naagin.proto import SupportsUpdateFlushEx


class MultiEncoding(SupportsUpdateFlushEx):
    def __init__(self, *encodings: SupportsUpdateFlushEx) -> None:
        self.encodings = encodings

    def update(self, data: bytes) -> bytes:
        for encoding in self.encodings:
            data = encoding.update(data)
        return data

    def flush(self, data: bytes = b"") -> bytes:
        for encoding in self.encodings:
            data = encoding.flush(data)
        return data
