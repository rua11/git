from sqlalchemy.orm import Session
from ..schemas import schemas
from ..models import school

def create_student(db: Session,classroom_id : int ,  student : schemas.StudentCreate):
    db_student = school.Student(**student.dict(), classroom_id = classroom_id)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_student_id(db : Session, student_id : int):
    return db.query(school.Student).filter(school.Student.student_id == student_id).first()

def get_student_name (db : Session, student_name :str):
    return db.query(school.Student).filter(school.Student.student_name == student_name).first()

def update_sutdent (db: Session, student_id: int , student : schemas.StudentUpdate):
    update_cl = db.query(school.Student).filter(school.Student.student_id == student_id).update(vars(student))
    db.commit()
    return get_student_id(db, student_id)

def delete_student(db:Session, student_id : int):
    delete_st = get_student_id(db, student_id)
    db.delete(delete_st)
    db.commit()
    
def create_subject_to_std(db: Session, student_id:int,  subject : schemas.SubjectCreate):
    # is_student = school.Student(**student.dict())
    is_student = db.query(school.Student).filter(school.Student.student_id == student_id).first()
    new_subject = school.Subject(subject_name = subject.subject_name)    
    is_student.subjects.append(new_subject)
    db.commit()
    return new_subject
    
    
def delete_sj_by_std (db: Session, student_id: int, subject_id: int):
    is_student = db.query(school.Student).filter(school.Student.student_id == student_id).first()
    is_subject = db.query(school.Subject).filter(school.Subject.subject_id == subject_id).first()
    is_student.subjects.remove(is_subject)
    db.commit()
    

