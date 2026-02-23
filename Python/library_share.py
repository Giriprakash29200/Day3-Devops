from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from datetime import date
from .lib_db import Base


class Issue(Base):
    __tablename__ = "issues"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    book_id = Column(Integer, ForeignKey("books.id"))
    issued_date = Column(Date, default=date.today)

    student = relationship("Student")
    book = relationship("Books")    