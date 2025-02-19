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
    request_parameter = sig.parameters.get("request")
    if request_parameter is None:
        for parameter in sig.parameters.values():
            if issubclass(parameter.annotation, Request):
                if request_parameter is None:
                    request_parameter = parameter
                else:
                    request_parameter = None
                    break
    if request_parameter is None:
        raise NotImplementedError
    argument_name = request_parameter.name
    key = awaitable.__name__

    @wraps(awaitable)
    async def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        bound = sig.bind(*args, **kwargs)
        bound.apply_defaults()

        request = bound.arguments.get(argument_name)
        if not isinstance(request, Request):
            raise NotImplementedError

        if not hasattr(request.state, key):
            result = await awaitable(*args, **kwargs)
            setattr(request.state, key, result)
        return getattr(request.state, key)

    return wrapper
