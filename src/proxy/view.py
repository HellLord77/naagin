import json
from json import JSONDecodeError
from typing import Optional

import mitmproxy
from mitmproxy.addonmanager import Loader
from mitmproxy.contentviews import TViewResult
from mitmproxy.contentviews import View
from mitmproxy.flow import Flow
from mitmproxy.http import HTTPFlow
from mitmproxy.http import Message

import utils


class ViewDOAXVVV(View):
    name = "DOAXVV"

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
            decrypted_data = utils.decrypt_message(flow.id, http_message)
            try:
                decoded_data = decrypted_data.decode()
            except UnicodeDecodeError:
                view_result = (
                    f"[{self.name}] Hex Dump",
                    mitmproxy.contentviews.format_text(decrypted_data.hex()),
                )
            else:
                try:
                    json_data = json.loads(decoded_data)
                except JSONDecodeError:
                    view_result = (
                        f"[{self.name}] Text",
                        mitmproxy.contentviews.format_text(decoded_data),
                    )
                else:
                    view_result = (
                        f"[{self.name}] JSON",
                        mitmproxy.contentviews.json.format_json(json_data),
                    )
            return view_result

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
            isinstance(flow, HTTPFlow) and utils.is_valid_message(flow.request, data)
        )


view = ViewDOAXVVV()


def load(_: Loader):
    mitmproxy.contentviews.add(view)


def done():
    mitmproxy.contentviews.remove(view)
