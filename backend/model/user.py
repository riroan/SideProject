from datetime import datetime
from model.base import Base

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"

    nickname: Mapped[str] = mapped_column(String(100))
    password: Mapped[str] = mapped_column(String(200))
    email: Mapped[str] = mapped_column(String(100))
    gender: Mapped[int] = mapped_column(Integer)
    birthday: Mapped[datetime] = mapped_column(DateTime)

    codes: Mapped[list["Code"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
