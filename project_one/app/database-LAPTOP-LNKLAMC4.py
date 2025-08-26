from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException

SQL_DB_URL = "sqlite:///./basenew.db"


engine = create_engine(SQL_DB_URL, connect_args={"check_same_thread": False})

session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()


def get_db():
    try:
        db = session_local()
        yield db
    except SQLAlchemyError as e:
        print(f"Ошибка базы данных: {e}")
        raise HTTPException(status_code=500, detail="Ошибка базы данных")
    finally:
        db.close()
