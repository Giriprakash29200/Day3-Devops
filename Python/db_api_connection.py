from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from pydantic import BaseModel
from typing import Optional
from .lib_db import SessionLocal
from .library_share import Issue as IssueModel

router = APIRouter()


class IssueCreate(BaseModel):
    student_id: int
    book_id: int


class IssueResponse(BaseModel):
    id: int
    student_id: int
    book_id: int
    student_name: Optional[str] = None
    student_department: Optional[str] = None
    book_name: Optional[str] = None
    book_author: Optional[str] = None

    class Config:
        from_attributes = True


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def build_response(issue):
    return {
        "id": issue.id,
        "student_id": issue.student_id,
        "book_id": issue.book_id,
        "student_name": issue.student.name if issue.student else None,
        "student_department": issue.student.department if issue.student else None,
        "book_name": issue.book.bookname if issue.book else None,
        "book_author": issue.book.author if issue.book else None,
    }


@router.get("/", response_model=list[IssueResponse])
def get_issues(db: Session = Depends(get_db)):
    issues = db.query(IssueModel).options(
        joinedload(IssueModel.student),
        joinedload(IssueModel.book)
    ).all()
    return [build_response(issue) for issue in issues]


@router.post("/", response_model=dict)
def create_issue(issue: IssueCreate, db: Session = Depends(get_db)):
    new_issue = IssueModel(student_id=issue.student_id, book_id=issue.book_id)
    db.add(new_issue)
    db.commit()

    new_issue = db.query(IssueModel).options(
        joinedload(IssueModel.student),
        joinedload(IssueModel.book)
    ).filter(IssueModel.id == new_issue.id).first()

    return {"message": "Issue created successfully", "data": build_response(new_issue)}


@router.put("/", response_model=dict)
def update_issue(id: int, issue: IssueCreate, db: Session = Depends(get_db)):
    existing_issue = db.query(IssueModel).filter(IssueModel.id == id).first()
    if not existing_issue:
        raise HTTPException(status_code=404, detail="Issue not found")
    existing_issue.student_id = issue.student_id
    existing_issue.book_id = issue.book_id
    db.commit()

    existing_issue = db.query(IssueModel).options(
        joinedload(IssueModel.student),
        joinedload(IssueModel.book)
    ).filter(IssueModel.id == id).first()

    return {"message": "Issue updated successfully", "data": build_response(existing_issue)}


@router.delete("/", response_model=dict)
def delete_issue(id: int, db: Session = Depends(get_db)):
    existing_issue = db.query(IssueModel).filter(IssueModel.id == id).first()
    if not existing_issue:
        raise HTTPException(status_code=404, detail="Issue not found")
    db.delete(existing_issue)
    db.commit()
    return {"message": "Issue deleted successfully"}