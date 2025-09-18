from ninja import Schema
from typing import Any

class CommonResponse(Schema):
    success: bool
    message: str
    data: Any = None
