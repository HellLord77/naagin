from datetime import datetime

from pydantic_xml import attr

from naagin.bases import AutoIndexXMLModelBase


class DirectoryAutoIndexXMLModel(AutoIndexXMLModelBase, tag="directory"):
    name: str
    mtime: datetime = attr()
