from pydantic import BaseModel, EmailStr
from app.database import Base


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class User_base(BaseModel):
    ID: int
    name: str

    class Config:
        orm_mode = True
