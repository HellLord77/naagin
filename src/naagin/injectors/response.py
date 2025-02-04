from http import HTTPStatus
from time import time

from fastapi import Response

from naagin import settings
from naagin.utils import DOAXVVHeader


def add_doaxvv_headers(response: Response):
    DOAXVVHeader.set(response, "ServerTime", int(time()))
    DOAXVVHeader.set(response, "Access-Token", "XPEACHACCESSTOKEN")
    DOAXVVHeader.set(response, "Status", HTTPStatus.OK)
    DOAXVVHeader.set(response, "ApplicationVersion", settings.version.application)
    DOAXVVHeader.set(response, "MasterVersion", settings.version.master)
    DOAXVVHeader.set(response, "ResourceVersion", settings.version.resource)
