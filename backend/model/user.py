from datetime import datetime

from model.base import Base
from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(Base):
    __tablename__ = "user"

    nickname: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(200))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    gender: Mapped[int] = mapped_column(Integer)
    birthday: Mapped[datetime] = mapped_column(DateTime)

    codes: Mapped[list["Code"]] = relationship("Code", back_populates="user")
