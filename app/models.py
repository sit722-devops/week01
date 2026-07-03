from pydantic import BaseModel, EmailStr


class Student(BaseModel):
    student_id: str
    name: str
    email: EmailStr
    program: str