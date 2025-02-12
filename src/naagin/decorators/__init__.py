from collections.abc import Callable
from functools import wraps
from inspect import signature

from fastapi import Request


def async_request_cache[T, **P](awaitable: Callable[P, T]) -> Callable[P, T]:
    @wraps(awaitable)
    async def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        sig = signature(awaitable)
        bound = sig.bind(*args, **kwargs)
        bound.apply_defaults()

        request = bound.arguments.get("request")
        if not isinstance(request, Request):
            raise NotImplementedError

        if not hasattr(request.state, awaitable.__name__):
            result = await awaitable(*args, **kwargs)
            setattr(request.state, awaitable.__name__, result)

        return getattr(request.state, awaitable.__name__)

    return wrapper
