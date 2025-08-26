from pydantic import BaseModel
from typing import Optional
from enum import Enum


class TaskStatus(str, Enum):
    new = "новая"
    in_progress = "в процессе"
    completed = "завершена"


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[TaskStatus] = TaskStatus.new


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None


class TaskRead(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: TaskStatus
    user_id: int

    class Config:
        orm_mode = True
