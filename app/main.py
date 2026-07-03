from fastapi import FastAPI, HTTPException
from app.models import Student
from app.students import students

app = FastAPI(
    title="Student Service",
    description="Week 1 microservice for the Campus Course Platform",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to the Student Service",
        "service": "student-service"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "student-service"
    }


@app.get("/students")
def get_students():
    return students


@app.get("/students/{student_id}")
def get_student(student_id: str):
    for student in students:
        if student["student_id"] == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


@app.post("/students", status_code=201)
def create_student(student: Student):

    for existing_student in students:
        if existing_student["student_id"] == student.student_id:
            raise HTTPException(
                status_code=400,
                detail="Student ID already exists"
            )

    students.append(student.model_dump())

    return student