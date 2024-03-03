from pydantic import BaseModel
from typing import Optional

class StudentRequest(BaseModel):
    first_name: str
    last_name: str
    class_standard: str
    class_section: str
    age: int
    gender: str
    phone_number: Optional[str] = None

    class config:
        orm_mode = True
