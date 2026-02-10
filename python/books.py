from pydantic import BaseModel

class Books(BaseModel):
    id: int
    bookname: str
    author: str

