from pydantic import ConfigDict

from naagin.models.base import CustomBaseModel


class CsvFileModel(CustomBaseModel):
    __pydantic_extra__: dict[str, str]

    file_encrypt_key: str

    model_config = ConfigDict(extra="allow")


class CsvListGetResponseModel(CustomBaseModel):
    csv_file_list: CsvFileModel
