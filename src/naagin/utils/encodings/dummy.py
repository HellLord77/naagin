from naagin.proto import SupportsUpdateFlushEx


class DummyEncoding(SupportsUpdateFlushEx):
    def update(self, data: bytes) -> bytes:
        return data

    def flush(self, data: bytes = b"") -> bytes:
        return data
