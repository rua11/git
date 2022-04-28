from fastapi import APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.constants.student_constants import StudentConstants
from app.database.get_db import get_db
from app.schemas import schemas

from app.crud import crud_classroom, crud_student

router = APIRouter(
    prefix="/students",
    tags= ["students"]
)
        

@router.post("/create_student/", response_model=schemas.Student)
def create_student(student : schemas.StudentCreate, classroom_id : int, db: Session = Depends(get_db)):
    student_db = crud_student.get_student_name(db=db, student_name= student.student_name)
    if student_db: 
        raise HTTPException(status_code=404, detail=StudentConstants.STUDENT_NOT_EXITS)
    return crud_student.create_student(db=db, student= student, classroom_id= classroom_id) 

@router.get("/student_id", response_model=schemas.Student)
def get_student_by_id(student_id : int, db: Session = Depends(get_db)):
    student_db = crud_student.get_student_id(db= db, student_id= student_id)
    if not student_db:
        raise HTTPException(status_code=404, detail="Sutdent ko ton tai")
    return student_db

@router.put("/student_cl", response_model= schemas.Student)
def update_student (student_id : int, classroom: schemas.StudentUpdate, db : Session = Depends(get_db)):
    st = crud_student.get_student_id(db, student_id)
    if not st: 
        raise HTTPException(status_code=404, detail= "dzdzdzd")
    update_student_db = crud_student.update_sutdent(db, student_id, classroom)
    return update_student_db

@router.delete("/delete")
def delete_student (student_id: int, db: Session = Depends(get_db)):
    delete_st = crud_student.get_student_id(db, student_id)
    if not delete_st:
        raise HTTPException(status_code=404, detail= "dzdzdzd")
    return crud_student.delete_student(db, student_id)
    
@router.post("/dasd", response_model=schemas.Subject)
def create_new(student_id : int, subject : schemas.SubjectCreate, db : Session = Depends(get_db)):
    return crud_student.create_subject_to_std(db= db, subject=subject, student_id= student_id)
    

@router.get("/student_s", response_model=schemas.StudentSubject)
def get_student_by_s(student_id : int, db: Session = Depends(get_db)):
    student_db = crud_student.get_student_id(db= db, student_id= student_id)
    # res= schemas.StudentSubject(**student_db.__dict__)
    return student_db


@router.delete("/dlt")
def delete_sj_by_std (student_id: int, subject_id: int ,db: Session = Depends(get_db)):
    
    crud_student.delete_sj_by_std(db, student_id= student_id, subject_id= subject_id)
    return {'thong bao': ' thanh cong'}
    