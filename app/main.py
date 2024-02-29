from fastapi import FastAPI, status
from app.api.v1 import students
from .database import engine
from app import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(students.router)


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/healthcheck", status_code=status.HTTP_200_OK)
def read_healthcheck():
    return {"status": "OK"}
