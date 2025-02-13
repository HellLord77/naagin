from pydantic import ConfigDict

from naagin.bases import ModelBase


class CsvFileModel(ModelBase):
    __pydantic_extra__: dict[str, str]

    file_encrypt_key: str

    model_config = ConfigDict(extra="allow")


class CsvListGetResponseModel(ModelBase):
    csv_file_list: CsvFileModel
