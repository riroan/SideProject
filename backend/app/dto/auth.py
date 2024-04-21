from datetime import datetime

from pydantic import BaseModel


class UserDTO(BaseModel):
    nickname: str
    email: str
    password: str
    gender: int
    birthday: datetime


class LoginDTO(BaseModel):
    email: str
    password: str
