import base64
import json
import logging
import os
import zlib
from typing import Optional

import cryptography.hazmat.primitives.asymmetric.rsa
import cryptography.hazmat.primitives.serialization
import mitmproxy.contentviews
import rich
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import CBC
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.primitives.serialization import Encoding
from cryptography.hazmat.primitives.serialization import PublicFormat
from mitmproxy.contentviews import TViewResult
from mitmproxy.contentviews import View
from mitmproxy.contentviews.json import ViewJSON
from mitmproxy.flow import Flow
from mitmproxy.http import HTTPFlow
from mitmproxy.http import Message
from mitmproxy.http import Request
from mitmproxy.http import Response

import config

PROXY_PRIVATE_KEY: RSAPrivateKey
PUBLIC_KEY: RSAPublicKey


def dump_private_key(private_key: RSAPrivateKey):
    private_key_bytes = private_key.private_bytes(
        cryptography.hazmat.primitives.serialization.Encoding.PEM,
        cryptography.hazmat.primitives.serialization.PrivateFormat.PKCS8,
        cryptography.hazmat.primitives.serialization.NoEncryption(),
    )
    with open(os.path.join(config.DATA_DIR, "private_key.pem"), "wb") as file:
        file.write(private_key_bytes)


def load_private_key() -> RSAPrivateKey:
    try:
        with open(os.path.join(config.DATA_DIR, "private_key.pem"), "rb") as file:
            private_key = (
                cryptography.hazmat.primitives.serialization.load_pem_private_key(
                    file.read(),
                    None,
                )
            )
    except FileNotFoundError:
        private_key = (
            cryptography.hazmat.primitives.asymmetric.rsa.generate_private_key(
                65537,
                2048,
            )
        )
        dump_private_key(private_key)
    return private_key


def redirect_request(request_: Request, path: str):
    logging.debug("[%s] %s %s", request_.method, path, request_.path)

    pretty_url = request_.pretty_url
    request_.scheme = "http"
    request_.host = config.SERVER_HOST
    request_.port = config.SERVER_PORT
    request_.path_components = path, *request_.path_components
    logging.info("[url] %s -> %s", pretty_url, request_.pretty_url)


def encrypt_data(data: bytes, initialization_vector: bytes) -> bytes:
    encryptor = Cipher(DOAXVV_VIEW.session_key, CBC(initialization_vector)).encryptor()
    padder = PKCS7(AES.block_size).padder()
    encrypted = padder.update(data) + padder.finalize()
    encrypted = encryptor.update(encrypted) + encryptor.finalize()
    encrypted = zlib.compress(encrypted)
    return encrypted


def decrypt_data(data: bytes, initialization_vector: bytes) -> bytes:
    decryptor = Cipher(DOAXVV_VIEW.session_key, CBC(initialization_vector)).decryptor()
    unpadder = PKCS7(AES.block_size).unpadder()
    decrypted = decryptor.update(data) + decryptor.finalize()
    decrypted = unpadder.update(decrypted) + unpadder.finalize()
    decrypted = zlib.decompress(decrypted)
    return decrypted


def print_json(request_: Request, response_: Optional[Response] = None):
    if response_ is None:
        response_ = request_
    if (
        request_.pretty_host == "api.doaxvv.com"
        and request_.path_components[:2] != ("v1", "session")
        and response_.content
    ):
        body = decrypt_data(
            response_.content,
            base64.b64decode(response_.headers["X-DOAXVV-Encrypted"]),
        )
        print(f"[{type(response_).__name__.lower()}] {request_.path}")
        rich.print_json(body.decode())


def running():
    global PROXY_PRIVATE_KEY

    PROXY_PRIVATE_KEY = load_private_key()


def requestheaders(flow: HTTPFlow):
    match flow.request.pretty_host:
        case "api.doaxvv.com":
            logging.debug("[%s] api %s", flow.request.method, flow.request.path)

            nonce = flow.request.headers["X-DOAXVV-Nonce"]
            proxy_nonce = os.urandom(4).hex()
            flow.request.headers["X-DOAXVV-Nonce"] = proxy_nonce
            logging.debug("[nonce] %s -> %s", nonce, proxy_nonce)

        case "api01.doaxvv.com":
            redirect_request(flow.request, "api01")

        case "game.doaxvv.com":
            redirect_request(flow.request, "game")


def request(flow: HTTPFlow):
    if (
        flow.request.method == "PUT"
        and flow.request.pretty_host == "api.doaxvv.com"
        and flow.request.path_components == ("v1", "session", "key")
    ):
        encrypt_key = flow.request.json()["encrypt_key"]
        session_key = PROXY_PRIVATE_KEY.decrypt(
            base64.b64decode(encrypt_key),
            PKCS1v15(),
        )
        DOAXVV_VIEW.session_key = AES(session_key)
        proxy_session_key = PUBLIC_KEY.encrypt(
            session_key,
            PKCS1v15(),
        )
        proxy_encrypt_key = base64.b64encode(proxy_session_key).decode()
        flow.request.text = json.dumps({"encrypt_key": proxy_encrypt_key})
        logging.debug("[session_key] %s -> %s", encrypt_key, proxy_encrypt_key)

    print_json(flow.request)


def response(flow: HTTPFlow):
    global PUBLIC_KEY

    if (
        flow.request.method == "GET"
        and flow.request.pretty_host == "api.doaxvv.com"
        and flow.request.path_components == ("v1", "session", "key")
    ):
        encrypt_key = flow.response.json()["encrypt_key"]
        PUBLIC_KEY = cryptography.hazmat.primitives.serialization.load_pem_public_key(
            encrypt_key.encode(),
        )
        proxy_public_key = PROXY_PRIVATE_KEY.public_key()
        proxy_encrypt_key = proxy_public_key.public_bytes(
            Encoding.PEM, PublicFormat.SubjectPublicKeyInfo
        ).decode()
        flow.response.text = json.dumps({"encrypt_key": proxy_encrypt_key})
        logging.debug("[public_key] %s -> %s", encrypt_key, proxy_encrypt_key)

    print_json(flow.request, flow.response)


class DOAXVVView(View):
    name = "DOAXVV"

    view_json = ViewJSON()
    session_key: Optional[AES] = None

    def __init__(self):
        old_self: Optional[DOAXVVView] = mitmproxy.contentviews.get(self.name)
        if old_self is not None:
            self.session_key = old_self.session_key
            mitmproxy.contentviews.remove(old_self)
        mitmproxy.contentviews.add(self)

    def __call__(
        self,
        data: bytes,
        *,
        content_type: Optional[str] = None,
        flow: Optional[Flow] = None,
        http_message: Optional[Message] = None,
        **unknown_metadata,
    ) -> TViewResult:
        if self.render_priority(
            data,
            content_type=content_type,
            flow=flow,
            http_message=http_message,
            **unknown_metadata,
        ):
            data = decrypt_data(
                data, base64.b64decode(http_message.headers["X-DOAXVV-Encrypted"])
            )
            return (
                "DOAXVV",
                self.view_json(
                    data,
                    content_type=content_type,
                    flow=flow,
                    http_message=http_message,
                    **unknown_metadata,
                )[1],
            )

    def render_priority(
        self,
        data: bytes,
        *,
        content_type: Optional[str] = None,
        flow: Optional[Flow] = None,
        http_message: Optional[Message] = None,
        **unknown_metadata,
    ) -> float:
        return bool(
            data
            and isinstance(flow, HTTPFlow)
            and (
                flow.request.pretty_host == "api.doaxvv.com"
                and flow.request.path_components[:2] != ("v1", "session")
            )
        )


DOAXVV_VIEW = DOAXVVView()
