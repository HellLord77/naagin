import base64
import hashlib
import zlib

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import CBC
from cryptography.hazmat.primitives.padding import PKCS7
from mitmproxy.http import Message
from mitmproxy.http import Request


def get_fernet(password: str) -> Fernet:
    return Fernet(base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest()))


def decrypt_data(algorithm: AES, data: bytes, initialization_vector: bytes) -> bytes:
    decryptor = Cipher(algorithm, CBC(initialization_vector)).decryptor()
    unpadder = PKCS7(AES.block_size).unpadder()
    decrypted = decryptor.update(data) + decryptor.finalize()
    decrypted = unpadder.update(decrypted) + unpadder.finalize()
    decrypted = zlib.decompress(decrypted)
    return decrypted


def is_valid_message(request: Request, content: bytes):
    return (
        request.pretty_host == "api.doaxvv.com"
        and request.path_components[:2] != ("v1", "session")
        and content
    )


def decrypt_message(key: str, message: Message) -> bytes:
    return decrypt_data(
        AES(get_fernet(key).decrypt(message.headers["Proxy-X-DOAXVV-Encrypted"])),
        message.content,
        base64.b64decode(message.headers["X-DOAXVV-Encrypted"]),
    )
