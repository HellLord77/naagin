import base64
import gzip
import hashlib
import zlib
from pathlib import Path

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
    decrypted_data = decryptor.update(data) + decryptor.finalize()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()
    return unpadded_data


def is_valid_message(request: Request, message: Message) -> bool:
    return bool(
        request.pretty_host == "api.doaxvv.com"
        and "X-DOAXVV-Encrypted" in message.headers
        and message.content
    )


def decrypt_message(key: str, message: Message) -> bytes:
    decrypted_data = decrypt_data(
        AES(get_fernet(key).decrypt(message.headers["Proxy-X-DOAXVV-Encrypted"])),
        message.content,
        base64.b64decode(message.headers["X-DOAXVV-Encrypted"]),
    )
    uncompressed_data = zlib.decompress(decrypted_data)
    return uncompressed_data


def decrypt_file(key: str, path: Path) -> bytes:
    decrypted_data = decrypt_data(
        AES(key.encode()),
        path.read_bytes(),
        bytes.fromhex(path.name),
    )
    uncompressed_data = gzip.decompress(decrypted_data)
    return uncompressed_data
