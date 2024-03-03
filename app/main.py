from contextlib import asynccontextmanager
from fastapi import FastAPI, status
from sqlalchemy import create_engine, text
import logging
from app.api.v1 import students
from .config import settings

# TODO:- add database migrations to the application
# TODO:- add logging to the application
# TODO:- add tests to the application

@asynccontextmanager
async def lifespan(app: FastAPI):
    # check if database exists, if not create it
    DATABASE_URI = f"postgresql://{settings.database_user}:{settings.database_password}@{settings.database_host}:{settings.database_port}/"
    engine = create_engine(DATABASE_URI)

    with engine.connect() as conn:
        # Check if database exists
        result = conn.execute(text(f"SELECT 1 FROM pg_database WHERE datname='{settings.database_name}'"))

        # If it doesn't exist, create it
        if not result.scalar():
            conn.execute(text("commit"))
            conn.execute(text(f"create database \"{settings.database_name}\""))
    yield

app = FastAPI(lifespan=lifespan)


app.include_router(students.router)


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/healthcheck", status_code=status.HTTP_200_OK)
def read_health_check():
    return {"status": "OK"}
