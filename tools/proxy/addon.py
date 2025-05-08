import base64
import json
import logging
import textwrap
from http import HTTPMethod
from typing import Awaitable
from typing import Callable
from typing import Optional
from weakref import WeakSet

import cryptography
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey
from cryptography.hazmat.primitives.serialization import Encoding
from cryptography.hazmat.primitives.serialization import PublicFormat
from mitmproxy import ctx
from mitmproxy.addonmanager import Loader
from mitmproxy.http import HTTPFlow

import config
import consts
import utils


class AddonDOAXVV:
    proxy_private_key: RSAPrivateKey

    public_key: Optional[RSAPublicKey] = None
    session_key: Optional[bytes] = None

    master_load_flow: Callable[[HTTPFlow], Awaitable[None]]

    loaded_flows: WeakSet[HTTPFlow] = WeakSet()

    async def load_flow(self, flow: HTTPFlow):
        self.loaded_flows.add(flow)
        await self.master_load_flow(flow)

    def load(self, _: Loader):
        self.proxy_private_key = utils.load_private_key()

        self.master_load_flow = ctx.master.load_flow
        ctx.master.load_flow = self.load_flow

    def done(self):
        ctx.master.load_flow = self.master_load_flow
        del self.master_load_flow

    def requestheaders(self, flow: HTTPFlow):
        if flow in self.loaded_flows:
            return

        match flow.request.pretty_host:
            case consts.API_HOST:
                if config.REAPI:
                    utils.redirect_request(flow.request, "api")
                else:
                    logging.info("[%s] %s", flow.request.method, flow.request.pretty_url)
                if config.RENONCE:
                    utils.renounce_request(flow.request)

            case consts.API01_HOST:
                if config.REAPI01:
                    utils.redirect_request(flow.request, "api01")
                else:
                    logging.info("[%s] %s", flow.request.method, flow.request.pretty_url)

            case consts.GAME_HOST:
                if config.REGAME:
                    utils.redirect_request(flow.request, "game")
                else:
                    logging.info("[%s] %s", flow.request.method, flow.request.pretty_url)

    def request(self, flow: HTTPFlow):
        if flow in self.loaded_flows:
            return

        if (
            flow.request.method == HTTPMethod.PUT
            and flow.request.pretty_host == consts.API_HOST
            and flow.request.path_components[-3:] == ("v1", "session", "key")
        ):
            encrypt_key = flow.request.json()["encrypt_key"]
            self.session_key = self.proxy_private_key.decrypt(
                base64.b64decode(encrypt_key),
                PKCS1v15(),
            )

            if self.public_key is None:
                return

            proxy_session_key = self.public_key.encrypt(
                self.session_key,
                PKCS1v15(),
            )
            proxy_encrypt_key = f"{"\r\n".join( textwrap.wrap(base64.b64encode(proxy_session_key).decode(),64))}\r\n"
            flow.request.text = json.dumps({"encrypt_key": proxy_encrypt_key})
            logging.info("[session_key] %s -> %s", encrypt_key, proxy_encrypt_key)

    def response(self, flow: HTTPFlow):
        if flow in self.loaded_flows:
            return

        if flow.request.pretty_host == consts.API_HOST:
            if flow.request.method == HTTPMethod.GET and flow.request.path_components[
                -3:
            ] == ("v1", "session", "key"):
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

                if encrypt_key == proxy_encrypt_key:
                    self.public_key = None
                    return

                flow.response.text = json.dumps({"encrypt_key": proxy_encrypt_key})
                logging.info("[public_key] %s -> %s", encrypt_key, proxy_encrypt_key)

            else:
                utils.write_flow(flow, self.session_key)


addons = [AddonDOAXVV()]
