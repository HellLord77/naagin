from collections.abc import Awaitable
from collections.abc import Callable
from functools import wraps
from inspect import signature

from fastapi import Request


def singleton[T, **P](cls: Callable[P, T], /) -> Callable[P, T]:
    self = None

    @wraps(cls)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        nonlocal self
        if self is None:
            self = cls(*args, **kwargs)
        return self

    return wrapper


def async_request_cache_unsafe[T: Awaitable, **P](awaitable: Callable[P, T], /) -> Callable[P, T]:
    sig = signature(awaitable)
    key = awaitable.__name__

    @wraps(awaitable)
    async def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        bound = sig.bind(*args, **kwargs)
        bound.apply_defaults()

        request = bound.arguments.get("request")
        if not isinstance(request, Request):
            raise NotImplementedError

        if not hasattr(request.state, key):
            result = await awaitable(*args, **kwargs)
            setattr(request.state, key, result)
        return getattr(request.state, key)

    return wrapper
