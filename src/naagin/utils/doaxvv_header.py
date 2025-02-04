from fastapi import Response


class DOAXVVHeader(str):
    def __new__(cls, alias: str):
        return super().__new__(cls, f"X-DOAXVV-{alias}")

    def lower(self):
        return self

    @classmethod
    def set(cls, response: Response, key: str, value):
        self = cls(key)
        response.headers[self] = str(value)
