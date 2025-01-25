class DOAXVVHeader(str):
    def __new__(cls, alias: str):
        return super().__new__(cls, f"X-DOAXVV-{alias}")

    def lower(self):
        return self
