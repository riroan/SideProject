from exceptions.base import BaseException
from fastapi import Request


def handle_error(app):

    @app.exception_handler(BaseException)
    async def base_exception_handler(request: Request, ex: BaseException):
        return "error"
