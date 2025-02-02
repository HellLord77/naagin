from secrets import randbelow
from secrets import token_hex
from string import ascii_lowercase
from string import digits

from . import choices


def access_token_factory() -> str:
    return token_hex(16)


def pinksid_factory() -> str:
    return "".join(choices(ascii_lowercase + digits, k=26))


def friend_code_factory() -> str:
    return f"{randbelow(1000):03}-{randbelow(1000):03}-{randbelow(1000):03}"
