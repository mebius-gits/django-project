from typing import Any
from ninja.responses import Response

def api_response(
    status: int = 200,
    success: bool = True,
    message: str = "",
    data: Any = None
) -> Response:
    return Response(
        {
            "success": success,
            "message": message,
            "data": data,
        },
        status=status
    )
