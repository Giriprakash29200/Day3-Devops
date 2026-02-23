from fastapi import FastAPI
from .lib_db import engine, Base

from . import models           
from . import studentmodel_api   
     

from .Dev import router as book_router
from .student_api import router as student_router



Base.metadata.create_all(bind=engine)

app = FastAPI(title="Library Management System")

app.include_router(book_router, prefix="/books", tags=["Books"])
app.include_router(student_router, prefix="/students", tags=["Students"])
