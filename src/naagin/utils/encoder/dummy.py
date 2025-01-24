from .base import BaseEncoder


class DummyEncoder(BaseEncoder):
    def update(self, data: bytes) -> bytes:
        return data

    def flush(self, data: bytes = b"") -> bytes:
        return data
