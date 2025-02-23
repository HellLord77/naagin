from pydantic_xml import RootXmlModel

from .directory import DirectoryAutoIndexXMLModel
from .file import FileAutoIndexXMLModel


class AutoIndexXMLModel(RootXmlModel, tag="list"):
    root: list[DirectoryAutoIndexXMLModel | FileAutoIndexXMLModel]
