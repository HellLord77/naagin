from enum import StrEnum


class NaaginHeaderEnum(StrEnum):
    PROCESS_TIME = "X-Naagin-Process-Time"
    SESSION_KEY = "X-Naagin-Session-Key"

    REQUEST_BODY = "X-Naagin-RequestBody"
    RESPONSE_BODY = "X-Naagin-ResponseBody"

    EXCEPTION_TYPE = "X-Naagin-Exception-Type"
    EXCEPTION_MESSAGE = "X-Naagin-Exception-Message"
