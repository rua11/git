from pydantic import BaseModel



class SubjectBase(BaseModel):
    subject_name: str
    
class SubjectCreate(SubjectBase):
    pass

class Subject(SubjectBase):
    
    subject_id : int
    # student_id : int
    class Config:
        orm_mode = True

class StudentBase(BaseModel):
    student_name : str
    student_age : int
    
class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    student_id : int
    classroom_id : int = None
    
    class Config:
        orm_mode = True

class StudentUpdate(StudentBase):
    classroom_id: int
    
class SubjectStudent(SubjectBase):
    students : list [Student] = []
    class Config:
        orm_mode = True

class StudentSubject (BaseModel):
    student_name : str
    student_age : int
    student_id : int
     
    subjects : list[Subject] = []
    
    class Config:
        orm_mode = True

        
class ClassroomBase(BaseModel):
    classroom_name : str
    classroom_teacher : str
    
class ClassroomCreate(ClassroomBase):
    pass

class Classroom(ClassroomBase):
    classroom_id : int
    students : list[Student] = []
    
    class Config:
        orm_mode = True
        
class ClassUpdate(ClassroomBase):
    pass

