from .database import Base
from sqlalchemy import TIMESTAMP, Column, Integer, String
from sqlalchemy.sql import text

class Student(Base):

    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    class_standard = Column(String, nullable=False)
    class_section = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    created_at = Column((TIMESTAMP(timezone=True)), nullable=False, server_default=text("now()"))
    gender = Column(String, nullable=False)
    phone_number = Column(String)
    temp = Column(String)
