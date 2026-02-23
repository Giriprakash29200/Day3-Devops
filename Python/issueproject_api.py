from fastapi import FastAPI
from .lib_db import engine, Base

from . import library_share
from . import models          # registers the 'books' table (Books class)
from . import studentdb_api   # registers the 'students' table (Student class)

from .db_api_connection import router as issue_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Database for student and Book related with Issues")

app.include_router(issue_router, prefix="/issues", tags=["issues"])