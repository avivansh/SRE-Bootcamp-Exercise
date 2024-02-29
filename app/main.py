from fastapi import FastAPI
from app.api.v1 import students
from .database import engine
from app import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(students.router)


@app.get("/")
def root():
    return {"message": "Hello World"}
