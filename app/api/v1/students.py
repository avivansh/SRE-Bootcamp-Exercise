from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ...database import get_db
from app import schemas, models


router = APIRouter(prefix="/api/v1/students", tags=["students"])


@router.get("/", status_code=status.HTTP_200_OK)
def get_students(db: Session = Depends(get_db)):
    students= db.query(models.Student).all()
    return students


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_student(payload: schemas.StudentRequest, db: Session = Depends(get_db)):
    new_student = models.Student(**payload.model_dump())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


@router.get("/{student_id}", status_code=status.HTTP_200_OK)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()

    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found in the database!")

    return student


@router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student_query = db.query(models.Student).filter(models.Student.id == student_id)
    student = student_query.first()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found in the database!")

    student_query.delete(synchronize_session=False)
    db.commit()

    return { "message": "Student deleted successfully!"}


@router.put("/{student_id}")
def update_student(student_id: int, payload: schemas.StudentRequest, db: Session = Depends(get_db)):
    student_query = db.query(models.Student).filter(models.Student.id == student_id)
    student = student_query.first()

    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found in the database!")

    student_query.update(payload.model_dump(), synchronize_session=False)
    db.commit()
    db.refresh(student)

    return student
