from fastapi import FastAPI
from app.models import school
from app.database.database import  engine
from app.router import rt_classroom, rt_student


school.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(rt_classroom.router)
app.include_router(rt_student.router)

