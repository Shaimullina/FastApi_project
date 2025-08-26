from fastapi import FastAPI, HTTPException, Path, Query, Body, Depends
from sqlalchemy.orm import Session
from app.main import get_db
from app.models.tasks import Base, Tasks
from app.models.user import User, Base
from app.database import engine, session_local, Base


from app.schemas.user import User_base, UserCreate
from app.schemas.task import Tasks_base, TasksCreate, TasksUpdate

app = FastAPI()


@app.post("/users", response_model=User_base)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(name=user.name, password=user.password, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
