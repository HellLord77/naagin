try:
    from anyio import Path as AsyncPath
except ImportError:
    try:
        from aiopath import AsyncPath
    except ImportError:
        from aiopathlib import AsyncPath

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

__all__ = ["AsyncPath", "JSONResponse", "json"]
