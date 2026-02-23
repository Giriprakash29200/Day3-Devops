from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .lib_db import Base          


class Books(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    bookname = Column(String)
    author = Column(String)

