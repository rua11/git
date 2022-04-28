from sqlalchemy.orm import Session
from ..schemas import schemas
from ..models import school

def create_classroom(db: Session, classroom: schemas.ClassroomCreate):
    db_classroom = school.Classroom(classroom_name = classroom.classroom_name, classroom_teacher = classroom.classroom_teacher)
    db.add(db_classroom)
    db.commit()
    db.refresh(db_classroom)
    return db_classroom

def get_class_id(db : Session, class_id : int):
    return db.query(school.Classroom).filter(school.Classroom.classroom_id == class_id).first()

def update_class(db: Session,class_id: int, classroom: schemas.ClassUpdate):
    update_cl = db.query(school.Classroom).filter(school.Classroom.classroom_id == class_id).update(vars(classroom))
    db.commit()
    return get_class_id(db, class_id)

def delete_class(db:Session, class_id : int):
    delete_cl = get_class_id(db, class_id)
    db.delete(delete_cl)
    db.commit()


    
