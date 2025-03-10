from pydantic import RootModel


class QuestCheckLicensePointPostResponseModel(RootModel[list]):
    root: list
