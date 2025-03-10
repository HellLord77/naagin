from pydantic import RootModel


class OwnerParameterAcceptPostResponseModel(RootModel[list]):
    root: list
