from typing import Any

from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import ORJSONResponse


class ResponseModelFactory:
    def __init__(self, status_type: str, status_code: str):
        self.status_type = status_type
        self.status_code = status_code

    def __call__(self, result: Any | None = None) -> ORJSONResponse:
        data = {"msg": self.status_type}
        if result:
            data["result"] = jsonable_encoder(result)
        return ORJSONResponse(data, status_code=self.status_code)


OK = ResponseModelFactory("ok", status.HTTP_200_OK)
CREATED = ResponseModelFactory("created", status.HTTP_201_CREATED)

BAD_REQUEST = ResponseModelFactory("bad_request", status.HTTP_400_BAD_REQUEST)
NOT_FOUND = ResponseModelFactory("not_found", status.HTTP_404_NOT_FOUND)
