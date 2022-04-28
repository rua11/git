from sqlalchemy import String, Integer, ForeignKey, Column
from sqlalchemy.orm import relationship
from ..database.database import Base 


class Classroom(Base):
    __tablename__ = 'classrooms'
    classroom_id = Column(Integer, primary_key = True)
    classroom_name = Column(String)
    classroom_teacher = Column(String)

    students = relationship('Student', back_populates = 'classrooms')
    
class Student(Base):
    __tablename__  = 'students'
    student_id = Column(Integer, primary_key = True)
    student_name = Column(String)
    student_age = Column(Integer)
    classroom_id = Column(Integer, ForeignKey('classrooms.classroom_id'))

    classrooms = relationship('Classroom', back_populates = 'students', lazy='joined')
    subjects = relationship('Subject', secondary = 'student_subject', lazy='joined')

class Subject (Base):
    __tablename__= 'subjects'
    subject_id = Column(Integer, primary_key = True)
    subject_name = Column(String)
    students = relationship(Student, secondary = 'student_subject', lazy='joined')

class Student_Subject(Base):
    __tablename__ = 'student_subject'
    student_id = Column(Integer, ForeignKey('students.student_id'), primary_key = True)
    subject_id = Column(Integer, ForeignKey('subjects.subject_id'), primary_key =  True)    