from abc import ABC
from abc import abstractmethod


class BaseEncoding(ABC):
    @abstractmethod
    def update(self, data: bytes) -> bytes:
        raise NotImplementedError

    @abstractmethod
    def flush(self) -> bytes:
        raise NotImplementedError
