from lxml.etree import Element
from lxml.etree import tostring

from .xml import XMLResponse


class LXMLResponse(XMLResponse):
    def render(self, content: Element) -> bytes:
        return tostring(content, encoding="utf-8")
