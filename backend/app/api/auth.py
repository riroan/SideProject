import bcrypt
import jwt
from app.depends.common import get_session, get_settings
from app.dto.auth import LoginDTO, UserDTO
from app.response import BAD_REQUEST, CREATED, NOT_FOUND, OK
from fastapi import APIRouter, Depends
from repository.user import UserRepository
from settings import Settings
from sqlalchemy.orm import Session

api = APIRouter()


@api.post("/register")
async def register(user_info: UserDTO, session: Session = Depends(get_session)):
    user_repository = UserRepository(session)

    encrypted_password = bcrypt.hashpw(user_info.password.encode(), bcrypt.gensalt())

    user_repository.save(
        nickname=user_info.nickname,
        email=user_info.email,
        password=encrypted_password,
        gender=user_info.gender,
        birthday=user_info.birthday,
    )

    return CREATED()


@api.post("/login")
async def login(
    login_info: LoginDTO,
    session: Session = Depends(get_session),
    settings: Settings = Depends(get_settings),
):
    user_repository = UserRepository(session)
    email = login_info.email
    password = login_info.password

    user = user_repository.get_by_email(email)

    if not user:
        return NOT_FOUND()

    check_password = bcrypt.checkpw(password.encode(), user.password.encode())
    if not check_password:
        return BAD_REQUEST()

    user_data = {}
    user_data["nickname"] = user.nickname
    user_data["email"] = user.email
    token = jwt.encode(user_data, settings.jwt_secret, settings.jwt_algorithm)

    return OK(token)
