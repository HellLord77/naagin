from cryptography.hazmat.primitives.ciphers import CipherContext

from .base import BaseEncoder


class CipherEncoder(BaseEncoder):
    def __init__(self, encryptor: CipherContext):
        self.encryptor = encryptor

    def update(self, data: bytes) -> bytes:
        return self.encryptor.update(data)

    def flush(self, data: bytes = b"") -> bytes:
        if data:
            data = self.encryptor.update(data)
        return data + self.encryptor.finalize()
