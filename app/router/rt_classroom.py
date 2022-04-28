from fastapi import APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.get_db import get_db
from app.schemas import schemas

from app.crud import crud_classroom

router = APIRouter(
    prefix="/classrooms",
    tags= ["classrooms"]
)
        

@router.post("/class/", response_model=schemas.Classroom)
def create_classroom(classroom : schemas.ClassroomCreate, db: Session = Depends(get_db)):
    return crud_classroom.create_classroom(db=db, classroom= classroom)

@router.get("/class_id", response_model=schemas.Classroom)
def get_class_by_id(class_id : int, db: Session = Depends(get_db)):
    class_db = crud_classroom.get_class_id(db= db, class_id= class_id)
    return class_db

@router.put("/update_cl", response_model= schemas.Classroom)
def update_class (class_id : int, classroom: schemas.ClassUpdate, db : Session = Depends(get_db)):
    cl = crud_classroom.get_class_id(db, class_id)
    if not cl: 
        raise HTTPException(status_code=404, detail= "dzdzdzd")
    update_class_db = crud_classroom.update_class(db, class_id, classroom)
    return update_class_db

@router.delete("/delete")
def delete_class (class_id: int, db: Session = Depends(get_db)):
    delete_st = crud_classroom.get_class_id(db, class_id)
    if not delete_st:
        raise HTTPException(status_code=404, detail= "dzdzdzd")
    return crud_classroom.delete_class(db, class_id)
    return {"thong bao": "da xóa"}
#jsaxsaxha shxa hsjjjjjjsahc ashs 
# son sua doan nay
# sa
# sa

#jjjjjjjsjdjasjdajsdjasd
#sdfsdfs
#aa
