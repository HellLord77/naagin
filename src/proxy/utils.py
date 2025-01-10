import base64
import hashlib
import logging
import os
import sys
import time
import zlib
from pathlib import Path
from typing import Optional

import cryptography.hazmat.primitives.asymmetric.rsa
import cryptography.hazmat.primitives.serialization
import rich
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import CBC
from cryptography.hazmat.primitives.padding import PKCS7
from mitmproxy.http import HTTPFlow
from mitmproxy.http import Message
from mitmproxy.http import Request
from mitmproxy.io import FlowWriter

import config

MITMWEB = Path(sys.argv[0]).name == "mitmweb"
FLOW_WRITER = FlowWriter(
    (config.DATA_DIR / "flows" / f"DOAXVV-{int(time.time())}.flows").open("wb")
)


def get_fernet(password: str) -> Fernet:
    return Fernet(base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest()))


def dump_private_key(private_key: RSAPrivateKey):
    private_key_bytes = private_key.private_bytes(
        cryptography.hazmat.primitives.serialization.Encoding.PEM,
        cryptography.hazmat.primitives.serialization.PrivateFormat.PKCS8,
        cryptography.hazmat.primitives.serialization.NoEncryption(),
    )
    (config.DATA_DIR / "private_key.pem").write_bytes(private_key_bytes)


def load_private_key() -> RSAPrivateKey:
    try:
        private_key_bytes = (config.DATA_DIR / "private_key.pem").read_bytes()
    except FileNotFoundError:
        private_key = (
            cryptography.hazmat.primitives.asymmetric.rsa.generate_private_key(
                65537,
                2048,
            )
        )
        dump_private_key(private_key)
    else:
        private_key = cryptography.hazmat.primitives.serialization.load_pem_private_key(
            private_key_bytes,
            None,
        )
    return private_key


def encrypt_data(algorithm: AES, data: bytes, initialization_vector: bytes) -> bytes:
    encryptor = Cipher(algorithm, CBC(initialization_vector)).encryptor()
    padder = PKCS7(AES.block_size).padder()
    encrypted = padder.update(data) + padder.finalize()
    encrypted = encryptor.update(encrypted) + encryptor.finalize()
    encrypted = zlib.compress(encrypted)
    return encrypted


def decrypt_data(algorithm: AES, data: bytes, initialization_vector: bytes) -> bytes:
    decryptor = Cipher(algorithm, CBC(initialization_vector)).decryptor()
    unpadder = PKCS7(AES.block_size).unpadder()
    decrypted = decryptor.update(data) + decryptor.finalize()
    decrypted = unpadder.update(decrypted) + unpadder.finalize()
    decrypted = zlib.decompress(decrypted)
    return decrypted


def renounce_request(request: Request):
    nonce = request.headers["X-DOAXVV-Nonce"]
    proxy_nonce = os.urandom(4).hex()
    request.headers["X-DOAXVV-Nonce"] = proxy_nonce
    logging.debug("[nonce] %s -> %s", nonce, proxy_nonce)


def redirect_request(request: Request, path: str):
    logging.debug("[%s] %s %s", request.method, path, request.path)

    pretty_url = request.pretty_url
    request.scheme = "http"
    request.host = config.SERVER_HOST
    request.port = config.SERVER_PORT
    request.path_components = path, *request.path_components
    logging.info("[url] %s -> %s", pretty_url, request.pretty_url)


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


def print_json(flow: HTTPFlow, session_key: Optional[bytes] = None):
    message = flow.request if flow.response is None else flow.response
    if is_valid_message(flow.request, message.content):
        if (
            session_key is not None
            and "Proxy-X-DOAXVV-Encrypted" not in message.headers
        ):
            message.headers["Proxy-X-DOAXVV-Encrypted"] = (
                get_fernet(flow.id).encrypt(session_key).decode()
            )

        if flow.response is not None:
            FLOW_WRITER.add(flow)

        if not MITMWEB:
            body = decrypt_message(flow.id, message)
            print(f"[{type(message).__name__.lower()}] {flow.request.path}")
            rich.print_json(body.decode())
