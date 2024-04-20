from fastapi import Request, status

from exceptions.base import BaseException

def handle_error(app):

    @app.exception_handler(BaseException)
    async def base_exception_handler(request: Request, ex: BaseException):
        return "error"

