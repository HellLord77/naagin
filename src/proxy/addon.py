import base64
import json
import logging
import textwrap
from http import HTTPMethod
from typing import Optional

import cryptography
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey
from cryptography.hazmat.primitives.serialization import Encoding
from cryptography.hazmat.primitives.serialization import PublicFormat
from mitmproxy.addonmanager import Loader
from mitmproxy.http import HTTPFlow

import consts
import utils


class AddonDOAXVV:
    proxy_private_key: RSAPrivateKey
    public_key: RSAPublicKey

    session_key: Optional[bytes] = None

    def load(self, _: Loader):
        self.proxy_private_key = utils.load_private_key()

    @staticmethod
    def requestheaders(flow: HTTPFlow):
        match flow.request.pretty_host:
            case consts.API_HOST:
                logging.debug("[%s] api %s", flow.request.method, flow.request.path)
                utils.renounce_request(flow.request)
            case consts.API01_HOST:
                if flow.request.path_components[:3] != ("v1", "johren", "authJohren"):
                    utils.redirect_request(flow.request, "api01")
            case consts.GAME_HOST:
                utils.redirect_request(flow.request, "game")

    def request(self, flow: HTTPFlow):
        if (
            flow.request.method == HTTPMethod.PUT
            and flow.request.pretty_host == consts.API_HOST
            and flow.request.path_components == ("v1", "session", "key")
        ):
            encrypt_key = flow.request.json()["encrypt_key"]
            session_key = self.proxy_private_key.decrypt(
                base64.b64decode(encrypt_key),
                PKCS1v15(),
            )
            self.session_key = session_key
            proxy_session_key = self.public_key.encrypt(
                session_key,
                PKCS1v15(),
            )
            proxy_encrypt_key = f"{"\r\n".join( textwrap.wrap(base64.b64encode(proxy_session_key).decode(),64))}\r\n"
            flow.request.text = json.dumps({"encrypt_key": proxy_encrypt_key})
            logging.info("[session_key] %s -> %s", encrypt_key, proxy_encrypt_key)
        else:
            utils.print_json(flow, self.session_key)

    def response(self, flow: HTTPFlow):
        if (
            flow.request.method == HTTPMethod.GET
            and flow.request.pretty_host == consts.API_HOST
            and flow.request.path_components == ("v1", "session", "key")
        ):
            encrypt_key = flow.response.json()["encrypt_key"]
            self.public_key = (
                cryptography.hazmat.primitives.serialization.load_pem_public_key(
                    encrypt_key.encode(),
                )
            )
            proxy_public_key = self.proxy_private_key.public_key()
            proxy_encrypt_key = proxy_public_key.public_bytes(
                Encoding.PEM, PublicFormat.SubjectPublicKeyInfo
            ).decode()
            flow.response.text = json.dumps({"encrypt_key": proxy_encrypt_key})
            logging.info("[public_key] %s -> %s", encrypt_key, proxy_encrypt_key)
        else:
            utils.print_json(flow, self.session_key)


addons = [AddonDOAXVV()]
