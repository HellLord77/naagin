from xml.etree.ElementTree import Element
from xml.etree.ElementTree import tostring

from starlette.responses import Response  # noqa: TID251


class XMLResponse(Response):
    media_type = "application/xml"

    def render(self, content: Element) -> bytes:
        return tostring(content, encoding="utf-8")
