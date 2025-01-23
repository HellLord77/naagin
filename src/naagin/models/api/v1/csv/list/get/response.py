from pydantic import ConfigDict

from naagin.models.base import BaseModel


class CsvFileModel(BaseModel):
    __pydantic_extra__: dict[str, str]

    file_encrypt_key: str

    model_config = ConfigDict(extra="allow")


class CsvListGetResponseModel(BaseModel):
    csv_file_list: CsvFileModel
