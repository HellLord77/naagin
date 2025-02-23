from datetime import datetime

from pydantic import ConfigDict
from pydantic_xml import BaseXmlModel  # noqa: TID251


class AutoIndexXMLModelBase(BaseXmlModel):
    model_config = ConfigDict(json_encoders={datetime: lambda value: value.strftime("%Y-%m-%dT%H:%M:%SZ")})
