from http import HTTPStatus
from time import time

from fastapi import Response

from naagin import settings
from naagin.exceptions import UnderMaintenanceNowException
from naagin.types.dependencies import MaintenanceDependency
from naagin.utils import CustomHeader


def check_maintenance(maintenance: MaintenanceDependency) -> None:
    if maintenance is not None:
        raise UnderMaintenanceNowException


def add_custom_headers(response: Response) -> None:
    CustomHeader.set(response, "ServerTime", int(time()))
    CustomHeader.set(response, "Access-Token", "XPEACHACCESSTOKEN")
    CustomHeader.set(response, "Status", HTTPStatus.OK)
    CustomHeader.set(response, "ApplicationVersion", settings.version.application)
    CustomHeader.set(response, "MasterVersion", settings.version.master)
    CustomHeader.set(response, "ResourceVersion", settings.version.resource)
