from typing import List
import pytest
import app.schemas as schemas

def test_create_student(client):
    response = client.post(
        "/api/v1/students/",
        json={
            "first_name": "abc",
            "last_name": "def",
            "class_standard": "12",
            "class_section": "A",
            "age": 17,
            "gender": "Male"
        }
    )
    student = schemas.StudentRequest(**response.json())
    assert response.status_code == 201
    assert student.first_name == "abc"
    assert student.last_name == "def"
    assert student.class_standard == "12"
    assert student.class_section == "A"
    assert student.age == 17
    assert student.gender == "Male"
    assert student.phone_number == None


def test_get_all_students(client, test_students):
    response = client.get("/api/v1/students/")
    students = [schemas.StudentResponse(**item) for item in response.json()]
    assert response.status_code == 200
    assert len(students) == 1
    assert students[0].first_name == test_students["first_name"]
    assert students[0].last_name == test_students["last_name"]
    assert students[0].class_standard == test_students["class_standard"]
    assert students[0].class_section == test_students["class_section"]
    assert students[0].age == test_students["age"]
    assert students[0].phone_number == test_students["phone_number"]


def test_get_student_by_id(client, test_students):
    response = client.get(f"/api/v1/students/{test_students['id']}")
    student = schemas.StudentResponse(**response.json())
    assert response.status_code == 200
    assert student.first_name == test_students["first_name"]
    assert student.last_name == test_students["last_name"]
    assert student.class_standard == test_students["class_standard"]
    assert student.class_section == test_students["class_section"]
    assert student.age == test_students["age"]
    assert student.phone_number == test_students["phone_number"]

def test_update_student(client, test_students):
    response = client.put(
        f"/api/v1/students/{test_students['id']}",
        json={
            "first_name": "pqr",
            "last_name": "xyz",
            "class_standard": "11",
            "class_section": "B",
            "age": 18,
            "gender": "Female",
            "phone_number": "1234567890"
        }
    )
    student = schemas.StudentResponse(**response.json())
    assert response.status_code == 200
    assert student.first_name == "pqr"
    assert student.last_name == "xyz"
    assert student.class_standard == "11"
    assert student.class_section == "B"
    assert student.age == 18
    assert student.phone_number == "1234567890"

def test_delete_student(client, test_students):
    response = client.delete(f"/api/v1/students/{test_students['id']}")
    assert response.status_code == 204
    response = client.get(f"/api/v1/students/{test_students['id']}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Student not found in the database!"}


