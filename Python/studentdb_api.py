from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .lib_db import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    department = Column(String, index=True)
