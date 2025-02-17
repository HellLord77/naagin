from naagin.abstract import BaseEncoding
from naagin.decorators import singleton


@singleton
class EmptyEncoding(BaseEncoding):
    def update(self, data: bytes) -> bytes:
        raise NotImplementedError

    def flush(self) -> bytes:
        raise NotImplementedError
