import base64
import zlib
from collections.abc import Generator

import config
import consts
import cryptography
import rich
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import CBC
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.primitives.serialization import Encoding
from cryptography.hazmat.primitives.serialization import NoEncryption
from cryptography.hazmat.primitives.serialization import PrivateFormat
from mitmproxy.http import HTTPFlow
from mitmproxy.http import Message
from mitmproxy.http import Request


def dump_private_key(private_key: RSAPrivateKey) -> None:
    private_key_bytes = private_key.private_bytes(Encoding.PEM, PrivateFormat.PKCS8, NoEncryption())
    (consts.CERT_DIR / "naagin-api.pem").write_bytes(private_key_bytes)


def load_private_key() -> RSAPrivateKey:
    try:
        private_key_bytes = (consts.CERT_DIR / "naagin-api.pem").read_bytes()
    except FileNotFoundError:
        private_key = cryptography.hazmat.primitives.asymmetric.rsa.generate_private_key(65537, 2048)
        dump_private_key(private_key)
    else:
        private_key = cryptography.hazmat.primitives.serialization.load_pem_private_key(private_key_bytes, None)
    return private_key


def decrypt_data(algorithm: AES, data: bytes, initialization_vector: bytes) -> bytes:
    decryptor = Cipher(algorithm, CBC(initialization_vector)).decryptor()
    unpadder = PKCS7(AES.block_size).unpadder()
    decrypted_data = decryptor.update(data) + decryptor.finalize()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()
    return unpadded_data  # noqa: RET504


def is_valid_message(request: Request, message: Message) -> bool:
    return bool(request.pretty_host in consts.API_HOSTS and "X-DOAXVV-Encrypted" in message.headers and message.content)


def iter_messages(flow: HTTPFlow) -> Generator[Message]:
    for message in (flow.request, flow.response):
        if is_valid_message(flow.request, message):
            yield message


def decrypt_message(key: str, message: Message) -> bytes:
    decrypted_data = decrypt_data(
        AES(base64.b64decode(key)), message.content, base64.b64decode(message.headers["X-DOAXVV-Encrypted"])
    )
    uncompressed_data = zlib.decompress(decrypted_data)
    return uncompressed_data  # noqa: RET504


def write_flow(flow: HTTPFlow, session_key: bytes | None = None) -> None:
    if session_key is not None:
        flow.comment = base64.b64encode(session_key).decode()

        if config.WRITE_FILE:
            consts.FLOW_WRITER.add(flow)

        if config.WRITE_CONSOLE:
            for message in iter_messages(flow):
                body = decrypt_message(flow.comment, message)
                print(f"[{type(message).__name__.lower()}] {flow.request.path}")  # noqa: T201
                rich.print_json(body.decode())
