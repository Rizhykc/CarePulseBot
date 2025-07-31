from sqlalchemy import Boolean, DateTime, ForeignKey, String, Text, func
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.orm import mapped_column as map_col

from conts import MAX_FIRSTNAME, MAX_TEXT, USER_NAME


class BaseModel(DeclarativeBase):
    created: Mapped[DateTime] = map_col(
        DateTime, default=func.now()
    )
    updated: Mapped[DateTime] = map_col(
        DateTime, default=func.now(), onupdate=func.now()
    )


class User(BaseModel):
    __tablename__ = 'user'

    user_id: Mapped[int] = map_col(primary_key=True, autoincrement=True)
    username: Mapped[str] = map_col(String(USER_NAME), nullable=False)
    first_name: Mapped[str] = map_col(String(MAX_FIRSTNAME), nullable=False)
    regist_date: Mapped[DateTime] = map_col(DateTime, default=func.now())
    last_active: Mapped[DateTime] = map_col(DateTime, default=func.now())


class Reminder(BaseModel):
    __tablename__ = 'reminder'

    reminder_id: Mapped[int] = map_col(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = map_col(ForeignKey(
        'user.user_id', ondelete='CASCADE'
    ), nullable=False)
    task_name: Mapped[String] = map_col(String(MAX_TEXT), nullable=False)
    reminder_time: Mapped[DateTime] = map_col(DateTime,)
    frequency: Mapped[Text] = map_col(Text,)
    is_active: Mapped[Boolean] = map_col(Boolean,)


class CompletedTask(BaseModel):
    __tablename__ = 'completed_task'

    entry_id: Mapped[int] = map_col(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = map_col(ForeignKey(
        'user.user_id', ondelete='CASCADE'
    ), nullable=False)
    task_name: Mapped[Text] = map_col(ForeignKey(
        'reminder.task_name', ondelete='CASCADE'
    ), nullable=False)
    completion_time: Mapped[DateTime] = map_col(DateTime,)
