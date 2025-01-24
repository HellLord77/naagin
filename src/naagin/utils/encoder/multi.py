from .base import BaseEncoder


class MultiEncoder(BaseEncoder):
    def __init__(self, *encoders: BaseEncoder):
        self.encoders = encoders

    def update(self, data: bytes) -> bytes:
        for encoder in self.encoders:
            data = encoder.update(data)
        return data

    def flush(self, data: bytes = b"") -> bytes:
        for encoder in self.encoders:
            data = encoder.flush(data)
        return data
