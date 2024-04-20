from typing import Any

from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import ORJSONResponse


class ResponseModelFactory:
    def __init__(self, status_type: str, status_code: str):
        self.status_type = status_type
        self.status_code = status_code

    def __call__(result: Any | None = None) -> ORJSONResponse:
        data = {"msg": "ok"}
        if result:
            data["result"] = jsonable_encoder(result)
        else:
            return ORJSONResponse(data, status_code=status.HTTP_200_OK)


OK = ResponseModelFactory("ok", status.HTTP_200_OK)
CREATED = ResponseModelFactory("created", status.HTTP_201_CREATED)
