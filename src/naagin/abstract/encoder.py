from abc import abstractmethod

from naagin.proto import SupportsUpdateFlushEx


class BaseEncoder(SupportsUpdateFlushEx):
    @abstractmethod
    def update(self, data: bytes) -> bytes:
        raise NotImplementedError

    @abstractmethod
    def flush(self, data: bytes = b"") -> bytes:
        raise NotImplementedError
