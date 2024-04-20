from app.depends.common import get_session
from app.dto.auth import UserDTO
from app.response import CREATED
from fastapi import APIRouter, Depends
from repository.user import UserRepository
from sqlalchemy.orm import Session

api = APIRouter()


@api.post("/register")
async def register(user_info: UserDTO, session: Session = Depends(get_session)):
    user_repository = UserRepository(session)

    user_repository.save(
        nickname=user_info.nickname,
        email=user_info.email,
        password=user_info.password,
        gender=user_info.gender,
        birthday=user_info.birthday,
    )

    return CREATED()
