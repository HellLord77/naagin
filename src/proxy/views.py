from typing import Optional

import mitmproxy.contentviews
from mitmproxy.contentviews import TViewResult
from mitmproxy.contentviews import View
from mitmproxy.contentviews.json import ViewJSON
from mitmproxy.flow import Flow
from mitmproxy.http import HTTPFlow
from mitmproxy.http import Message

import utils


class DOAXVVView(View):
    name = "DOAXVV"

    view_json = ViewJSON()

    def __init__(self):
        old_self: Optional[DOAXVVView] = mitmproxy.contentviews.get(self.name)
        if old_self is not None:
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
            return (
                "DOAXVV",
                self.view_json(
                    utils.decrypt_message(flow.id, http_message),
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
            isinstance(flow, HTTPFlow) and utils.is_valid_message(flow.request, data)
        )
