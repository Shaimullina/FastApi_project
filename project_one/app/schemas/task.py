from pydantic import BaseModel
from app.schemas.user import User
from typing import Literal, Optional
from app.database import Base

VALID_STATUSES = Literal["новая", "в процессе", "завершена"]


class TasksCreate(BaseModel):
    title: str
    description: str
    user_id: int
    status: VALID_STATUSES


class Tasks_base(BaseModel):
    ID: int
    title: str
    user_id: int
    status: VALID_STATUSES
    user: User

    class Config:
        orm_mode = True


class TasksUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[VALID_STATUSES] = None
