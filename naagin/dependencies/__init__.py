from http import HTTPStatus
from time import time

from fastapi import Request
from fastapi import Response
from starlette.datastructures import MutableHeaders

from naagin.enums import DOAXVVHeaderEnum
from naagin.exceptions import UnderMaintenanceNowException
from naagin.types_.dependencies import MaintenanceDependency
from naagin.types_.headers import ApplicationVersionHeader
from naagin.types_.headers import MasterVersionHeader
from naagin.types_.headers import ResourceVersionHeader
from naagin.utils import DOAXVVHeader


def check_maintenance(maintenance: MaintenanceDependency) -> None:
    if maintenance is not None:
        raise UnderMaintenanceNowException


def remove_master_version_header(request: Request) -> None:
    if request.headers.get(DOAXVVHeaderEnum.MASTER_VERSION) == "0":
        headers = MutableHeaders(raw=request.scope["headers"])
        del headers[DOAXVVHeaderEnum.MASTER_VERSION]


def add_custom_headers(
    response: Response,
    application_version: ApplicationVersionHeader,
    master_version: MasterVersionHeader,
    resource_version: ResourceVersionHeader,
) -> None:
    response.headers[DOAXVVHeader(DOAXVVHeaderEnum.SERVER_TIME)] = str(int(time()))
    response.headers[DOAXVVHeader(DOAXVVHeaderEnum.ACCESS_TOKEN)] = "XPEACHACCESSTOKEN"
    response.headers[DOAXVVHeader(DOAXVVHeaderEnum.STATUS)] = str(HTTPStatus.OK)

    response.headers[DOAXVVHeader(DOAXVVHeaderEnum.APPLICATION_VERSION)] = str(application_version)
    response.headers[DOAXVVHeader(DOAXVVHeaderEnum.MASTER_VERSION)] = str(master_version)
    response.headers[DOAXVVHeader(DOAXVVHeaderEnum.RESOURCE_VERSION)] = resource_version
