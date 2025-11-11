import json
from json import JSONDecodeError

from mitmproxy import contentviews
from mitmproxy.contentviews import Contentview
from mitmproxy.contentviews import Metadata
from mitmproxy.http import HTTPFlow
from mitmproxy.http import Message

import utils


class DOAXVVContentview(Contentview):
    syntax_highlight = "yaml"

    def prettify(self, _: bytes, metadata: Metadata) -> str:
        decrypted_data = utils.decrypt_message(
            metadata.flow.comment, metadata.http_message
        )
        try:
            decoded_data = decrypted_data.decode()
        except UnicodeDecodeError:
            view_result = decrypted_data.hex()
        else:
            try:
                json_data = json.loads(decoded_data)
            except JSONDecodeError:
                view_result = decoded_data
            else:
                view_result = json.dumps(json_data, indent=4, ensure_ascii=False)
        return view_result

    def render_priority(self, _: bytes, metadata: Metadata) -> float:
        return (
            isinstance(metadata.flow, HTTPFlow)
            and isinstance(metadata.http_message, Message)
            and utils.is_valid_message(metadata.flow.request, metadata.http_message)
        )


contentviews.add(DOAXVVContentview)
