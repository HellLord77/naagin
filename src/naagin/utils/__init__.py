from collections.abc import Sequence
from secrets import choice

from fastapi.datastructures import Headers
from starlette.routing import Match
from starlette.routing import Router
from starlette.types import Scope

from .custom_header import CustomHeader as CustomHeader
from .singleton_meta import SingletonMeta as SingletonMeta
from .sqlalchemy_handler import SQLAlchemyHandler as SQLAlchemyHandler


def choices[T: Sequence](population: T, *, k: int = 1) -> list[T]:
    return [choice(population) for _ in range(k)]


def headers_get_split(self: Headers, key: str) -> list[str]:
    value = self.get(key, "")
    return list(filter(None, map(str.strip, value.split(","))))


def router_matches(self: Router, scope: Scope) -> tuple[Match, Scope]:
    partial_matches: tuple[Match, Scope] = Match.NONE, {}
    for route in self.routes:
        matches = route.matches(scope)
        match matches[0]:
            case Match.FULL:
                return matches
            case Match.PARTIAL if partial_matches[0] == Match.NONE:
                partial_matches = matches
    return partial_matches
