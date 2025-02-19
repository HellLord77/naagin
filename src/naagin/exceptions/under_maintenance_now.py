from http import HTTPStatus

from naagin.bases import ExceptionBase


class UnderMaintenanceNowException(ExceptionBase):
    code = HTTPStatus.SERVICE_UNAVAILABLE
    message = "under maintenance now"
