from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import Student
from schemas import StudentCreate
from database import get_db

router = APIRouter()

@router.post("/students")
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    new_student = Student(name=student.name, email=student.email, course=student.course)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student
