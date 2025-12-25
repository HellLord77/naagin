try:
    import orjson as json
except ImportError:
    try:
        import ujson as json
    except ImportError:
        import json

        from fastapi.responses import JSONResponse
    else:
        from fastapi.responses import UJSONResponse as JSONResponse
else:
    from fastapi.responses import ORJSONResponse as JSONResponse

__all__ = ["JSONResponse", "json"]
