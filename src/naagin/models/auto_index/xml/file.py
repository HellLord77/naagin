from datetime import datetime

from pydantic_xml import attr

from naagin.bases import AutoIndexXMLModelBase


class FileAutoIndexXMLModel(AutoIndexXMLModelBase, tag="file"):
    name: str
    mtime: datetime = attr()
    size: int = attr()
