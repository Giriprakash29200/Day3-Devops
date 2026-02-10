from fastapi import FastAPI
from .studentlist import Student
from pydantic import BaseModel

app = FastAPI()

# ---------------- STUDENTS ----------------

slist = [
    Student(id=1, name="Giri Prakash", department="Electronics And Communication Engineering"),
    Student(id=2, name="Murugar", department="Electronics and Communication Engineering")
]

@app.get("/students")
def get_students():
    return slist

# ---------------- BOOKS ----------------

class Book(BaseModel):
    id: int
    bookname: str
    author: str

blist = [
    Book(id=1, bookname="Computer Networks", author="Network Engineer"),
    Book(id=2, bookname="Cloud Computing", author="AWS")
]

@app.get("/books")
def get_books():
    return blist

@app.post("/books")
def add_books(book: Book):
    blist.append(book)
    return {
        "message": "Book Added Successfully!",
        "data": book
    }
