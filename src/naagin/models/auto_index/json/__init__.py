from pydantic import RootModel

from .directory import DirectoryAutoIndexModel
from .file import FileAutoIndexModel


class AutoIndexModel(RootModel):
    root: list[DirectoryAutoIndexModel | FileAutoIndexModel]
