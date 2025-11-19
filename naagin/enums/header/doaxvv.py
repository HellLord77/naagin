from enum import StrEnum


class DOAXVVHeaderEnum(StrEnum):
    ACCESS_TOKEN = "X-DOAXVV-Access-Token"  # noqa: S105
    CLIENT_TYPE = "X-DOAXVV-ClientType"
    NONCE = "X-DOAXVV-Nonce"

    SERVER_TIME = "X-DOAXVV-ServerTime"
    STATUS = "X-DOAXVV-Status"

    APPLICATION_VERSION = "X-DOAXVV-ApplicationVersion"
    MASTER_VERSION = "X-DOAXVV-MasterVersion"
    RESOURCE_VERSION = "X-DOAXVV-ResourceVersion"

    ENCODING = "X-DOAXVV-Encoding"
    ENCRYPTED = "X-DOAXVV-Encrypted"
