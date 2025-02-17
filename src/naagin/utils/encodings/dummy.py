from naagin.abstract import BaseEncoding
from naagin.decorators import singleton


@singleton
class DummyEncoding(BaseEncoding):
    def update(self, data: bytes) -> bytes:
        return data

    def flush(self) -> bytes:
        return b""
