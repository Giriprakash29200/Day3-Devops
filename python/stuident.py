from fastapi import FastAPI
from .studentlist import Student
from .books import Books
from pydantic import BaseModel


app = FastAPI()

slist = [
    Student(id = 1, name = "Giri Prakash", department = "Electronics And Communication Engineering"),
    Student(id = 2, name = "Murugar", department = "Electronics and Communication Engineering")
]

blist = [
    Books(id = 1, bookname= "Computer Networks", author= "Network Engineer"),
    Books(id = 2, bookname= "Cloud  Computing", author= "AWS")
]

@app.get("/students")
def get_students():
    return slist

@app.get("/student/{id}")
def get_id(id :int):
    return slist[id -1]

@app.get("/books")
def get_books():
    return blist

@app.get("/books/{id}")
def get_booksid(id :int):
    return blist[id -1]


@app.post("/book")
def add_books(book : Books):
    blist.append(book)
    return "Book Added Successfully!"





