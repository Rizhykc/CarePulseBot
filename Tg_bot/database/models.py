from sqlalchemy import DateTime, String, Text, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class BaseModel(DeclarativeBase):
    created: Mapped[DateTime] = mapped_column(
        DateTime, default=func.now()
    )
    updated: Mapped[DateTime] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now()
    )


class Users(BaseModel):
    __tablename__ = 'User'

    user_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(150), nullable=False)
    first_name: Mapped[str] = mapped_column(String(20), nullable=False)
    regist_date: Mapped[DateTime] = mapped_column(DateTime,)
    last_active: Mapped[DateTime] = mapped_column(DateTime,)
