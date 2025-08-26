from fastapi import FastAPI, Depends
from app.database import engine, get_db, Base
from app import auth
from app.models import tasks, user

from app.schemas import user as user_schemas
from app.schemas import task as task_schemas

from app.routers import user, tasks


app = FastAPI()

Base.metadata.create_all(bind=engine)


app.include_router(user.router, prefix="/users", dependencies=[Depends(get_db)])

app.include_router(tasks.router, prefix="/tasks", dependencies=[Depends(get_db)])
