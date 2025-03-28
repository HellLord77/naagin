from typing import Literal

from pydantic import ConfigDict

from naagin.bases import ModelBase
from naagin.types.fields import CSVField
from naagin.types.fields import MD5Field


class CSVFileModel(ModelBase):
    __pydantic_extra__: dict[CSVField, MD5Field]

    file_encrypt_key: Literal["9AraWdtpsar4fln2r1TtX0AxiCJcLSqp"]

    model_config = ConfigDict(extra="allow")


class CSVListGetResponseModel(ModelBase):
    csv_file_list: CSVFileModel
