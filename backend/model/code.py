from model.base import Base
from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Code(Base):
    __tablename__ = "code"

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    language: Mapped[str] = mapped_column(String(100))
    code: Mapped[str] = mapped_column(Text)

    user: Mapped["User"] = relationship("User", back_populates="codes")
