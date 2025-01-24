from abc import ABC
from abc import abstractmethod


class BaseEncoder(ABC):
    @abstractmethod
    def update(self, data: bytes) -> bytes:
        raise NotImplementedError

    @abstractmethod
    def flush(self, data: bytes = b"") -> bytes:
        raise NotImplementedError
