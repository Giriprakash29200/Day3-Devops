from fastapi import FastAPI
from .studentlist import Student
from .books import Books

app = FastAPI()

blist = [
    Books(id=1, bookname="Computer Networks", author="Network Engineer"),
    Books(id=2, bookname="Cloud Computing", author="AWS")
]

@app.get("/books")
def get_books():
    return blist

@app.post("/books")
def add_books(giri: Books):
    blist.append(giri)
    return {
        "message": "Book Added Successfully!",
        "data": giri
    }

@app.put("/books")
def update_books(id: int, product:Books):
    for i in range(len(blist)):
        if blist[i].id == id:
            blist[i] = product
            return "Book updated Successfully"
    return "book not found"

@app.delete("/books")
def delete_books(id :int):
    for i in range(len(blist)):
        if blist[i].id ==id:
            del blist [i]
            return "Book was delete"
        
