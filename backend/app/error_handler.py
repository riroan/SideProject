from app.exceptions.auth import DuplicatedUserException
from app.exceptions.base import BaseException
from app.response import BAD_REQUEST
from fastapi import Request
from sqlalchemy.exc import IntegrityError


def handle_error(app):

    @app.exception_handler(BaseException)
    async def base_exception_handler(request: Request, ex: BaseException):
        return "error"

    @app.exception_handler(IntegrityError)
    async def db_exception(request: Request, ex: IntegrityError):
        return BAD_REQUEST()
