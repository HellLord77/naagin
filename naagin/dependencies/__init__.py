from http import HTTPStatus
from time import time

from fastapi import Request
from fastapi import Response
from starlette.datastructures import MutableHeaders

from naagin.exceptions import UnderMaintenanceNowException
from naagin.types_.dependencies import MaintenanceDependency
from naagin.types_.headers import ApplicationVersionHeader
from naagin.types_.headers import MasterVersionHeader
from naagin.types_.headers import ResourceVersionHeader
from naagin.utils import CustomHeader


def check_maintenance(maintenance: MaintenanceDependency) -> None:
    if maintenance is not None:
        raise UnderMaintenanceNowException


def remove_master_version_header(request: Request) -> None:  # deprecated
    headers = MutableHeaders(raw=request.scope["headers"])
    if headers.get("X-DOAXVV-MasterVersion") == "0":
        del headers["X-DOAXVV-MasterVersion"]


def add_custom_headers(
    response: Response,
    application_version: ApplicationVersionHeader,
    master_version: MasterVersionHeader,
    resource_version: ResourceVersionHeader,
) -> None:
    CustomHeader.set(response, "ServerTime", int(time()))
    CustomHeader.set(response, "Access-Token", "XPEACHACCESSTOKEN")
    CustomHeader.set(response, "Status", HTTPStatus.OK)
    CustomHeader.set(response, "ApplicationVersion", application_version)
    CustomHeader.set(response, "MasterVersion", master_version)
    CustomHeader.set(response, "ResourceVersion", resource_version)
