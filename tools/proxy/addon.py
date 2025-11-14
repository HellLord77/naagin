import base64
import json
import logging
import secrets
import textwrap
from collections.abc import Awaitable
from collections.abc import Callable
from http import HTTPMethod
from weakref import WeakSet

import config
import consts
import cryptography
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey
from cryptography.hazmat.primitives.serialization import Encoding
from cryptography.hazmat.primitives.serialization import PublicFormat
from mitmproxy import ctx
from mitmproxy.addonmanager import Loader
from mitmproxy.http import HTTPFlow
from mitmproxy.http import Request

import utils

logger = logging.getLogger(__name__)


def redirect_request(request: Request, path: str) -> None:
    pretty_host = request.pretty_host

    pretty_url = request.pretty_url
    request.scheme = consts.SERVER_URL.scheme
    request.host = consts.SERVER_URL.hostname
    request.port = consts.SERVER_URL.port
    request.path_components = path, *request.path_components

    logger.info("[url] %s -> %s", pretty_url, request.url)
    request.headers["Host"] = pretty_host


def renounce_request(request: Request) -> None:
    nonce = request.headers["X-DOAXVV-Nonce"]
    proxy_nonce = secrets.token_hex(4)
    request.headers["X-DOAXVV-Nonce"] = proxy_nonce
    logger.info("[nonce] %s -> %s", nonce, proxy_nonce)


class DOAXVVAddon:
    proxy_private_key: RSAPrivateKey

    public_key: RSAPublicKey | None = None
    session_key: bytes | None = None

    master_load_flow: Callable[[HTTPFlow], Awaitable[None]]

    loaded_flows: WeakSet[HTTPFlow] = WeakSet()

    async def load_flow(self, flow: HTTPFlow) -> None:
        self.loaded_flows.add(flow)
        await self.master_load_flow(flow)

    def load(self, _: Loader) -> None:
        self.proxy_private_key = utils.load_private_key()

        self.master_load_flow = ctx.master.load_flow
        ctx.master.load_flow = self.load_flow

        logger.info("[addon] load")

    def done(self) -> None:
        ctx.master.load_flow = self.master_load_flow
        del self.master_load_flow

        logger.info("[addon] done")

    def requestheaders(self, flow: HTTPFlow) -> None:
        if flow in self.loaded_flows:
            return

        match flow.request.pretty_host:
            case consts.API_HOST | consts.API_JP_HOST:
                logger.info("[api] %s: %s", flow.request.method, flow.request.pretty_url)
                if config.REAPI:
                    redirect_request(flow.request, "api")
                if config.RENONCE:
                    renounce_request(flow.request)

            case consts.API01_HOST | consts.API01_JP_HOST:
                logger.info("[api01] %s: %s", flow.request.method, flow.request.pretty_url)
                if config.REAPI01:
                    redirect_request(flow.request, "api01")

            case consts.GAME_HOST:
                logger.info("[game] %s: %s", flow.request.method, flow.request.pretty_url)
                if config.REGAME:
                    redirect_request(flow.request, "game")

            case consts.CDN01_HOST:
                logger.info("[cdn01] %s: %s", flow.request.method, flow.request.pretty_url)
                if config.RECDN01:
                    redirect_request(flow.request, "cdn01")

    def request(self, flow: HTTPFlow) -> None:
        if flow in self.loaded_flows:
            return

        if (
            flow.request.method == HTTPMethod.PUT
            and (flow.request.pretty_host in consts.API_HOSTS)
            and flow.request.path_components[-3:] == ("v1", "session", "key")
        ):
            encrypt_key = flow.request.json()["encrypt_key"]
            self.session_key = self.proxy_private_key.decrypt(base64.b64decode(encrypt_key), PKCS1v15())

            if self.public_key is None:
                return

            proxy_session_key = self.public_key.encrypt(self.session_key, PKCS1v15())
            proxy_encrypt_key = f"{'\r\n'.join(textwrap.wrap(base64.b64encode(proxy_session_key).decode(), 64))}\r\n"
            flow.request.text = json.dumps({"encrypt_key": proxy_encrypt_key})
            logger.info("[session_key] %s -> %s", encrypt_key, proxy_encrypt_key)

    def response(self, flow: HTTPFlow) -> None:
        if flow in self.loaded_flows:
            return

        if flow.request.pretty_host in consts.API_HOSTS:
            if flow.request.method == HTTPMethod.GET and flow.request.path_components[-3:] == ("v1", "session", "key"):
                encrypt_key = flow.response.json()["encrypt_key"]
                self.public_key = cryptography.hazmat.primitives.serialization.load_pem_public_key(encrypt_key.encode())
                proxy_public_key = self.proxy_private_key.public_key()
                proxy_encrypt_key = proxy_public_key.public_bytes(
                    Encoding.PEM, PublicFormat.SubjectPublicKeyInfo
                ).decode()

                if encrypt_key == proxy_encrypt_key:
                    self.public_key = None
                    return

                flow.response.text = json.dumps({"encrypt_key": proxy_encrypt_key})
                logger.info("[public_key] %s -> %s", encrypt_key, proxy_encrypt_key)

            else:
                utils.write_flow(flow, self.session_key)


addons = [DOAXVVAddon()]
