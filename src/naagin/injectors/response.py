from http import HTTPStatus
from time import time

from fastapi import Response

from naagin import settings
from naagin.utils import CustomHeader


def add_custom_headers(response: Response) -> None:
    CustomHeader.set(response, "ServerTime", int(time()))
    CustomHeader.set(response, "Access-Token", "XPEACHACCESSTOKEN")
    CustomHeader.set(response, "Status", HTTPStatus.OK)
    CustomHeader.set(response, "ApplicationVersion", settings.version.application)
    CustomHeader.set(response, "MasterVersion", settings.version.master)
    CustomHeader.set(response, "ResourceVersion", settings.version.resource)
