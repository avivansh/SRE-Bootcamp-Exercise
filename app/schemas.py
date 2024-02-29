from pydantic import BaseModel


class StudentRequest(BaseModel):
    first_name: str
    last_name: str
    class_standard: str
    class_section: str
    age: int

    class config:
        orm_mode = True
