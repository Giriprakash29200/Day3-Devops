from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

issue = relationship("Issue", back_populates="books")

db_url = "postgresql://postgres:1234@localhost:5432/book_list"

engine = create_engine(db_url)

SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)

Base = declarative_base()
