from http import HTTPStatus

from naagin import settings
from naagin.bases import ExceptionBase

logger = settings.logging.logger


class InternalServerErrorException(ExceptionBase):
    code = HTTPStatus.INTERNAL_SERVER_ERROR
    message = "internal server error"
