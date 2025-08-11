from fastapi import FastAPI, HTTPException, Path, Query, Body, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.database import engine, get_db, session_local, Base

from app.models import tasks, user

from app.schemas import user as user_schemas
from app.schemas import task as task_schemas

from app.routers import user, tasks


app = FastAPI()

Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = session_local()
        yield db
    except SQLAlchemyError as e:
        print(f"Ошибка базы данных: {e}")
        raise HTTPException(status_code=500, detail="Ошибка базы данных")
    finally:
        db.close()


app.include_router(user.router, prefix="/users")

app.include_router(tasks.router, prefix="/tasks", dependencies=[Depends(get_db)])
