import json
from decimal import Decimal

from fastapi.responses import JSONResponse


class _DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)


def success_response(data, status_code=200):
    """Backward-compatible name. Use the same serializer as success_response_safe."""
    return success_response_safe(data, status_code)


def success_response_safe(data, status_code=200):
    """Serializes Decimal (and other non-JSON types) via the custom encoder."""
    return JSONResponse(
        status_code=status_code,
        content=json.loads(json.dumps({"success": True, "data": data}, cls=_DecimalEncoder)),
    )


def error_response(message, status_code=400):
    return JSONResponse(status_code=status_code, content={"success": False, "error": message})
