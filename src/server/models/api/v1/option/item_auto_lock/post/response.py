from pydantic import RootModel


class OptionItemAutoLockPostResponseModel(RootModel[list]):
    root: list
