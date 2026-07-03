
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["service"] == "student-service"


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_get_all_students():
    response = client.get("/students")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 3


def test_get_student_by_id():
    response = client.get("/students/S100001")

    assert response.status_code == 200
    assert response.json()["student_id"] == "S100001"
    assert response.json()["name"] == "John Smith"


def test_get_student_not_found():
    response = client.get("/students/S999999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Student not found"


def test_create_student():
    new_student = {
        "student_id": "S100010",
        "name": "Sophia Taylor",
        "email": "sophia.taylor@deakin.edu.au",
        "program": "Master of Software Engineering"
    }

    response = client.post("/students", json=new_student)

    assert response.status_code == 201
    assert response.json()["student_id"] == "S100010"
    assert response.json()["name"] == "Sophia Taylor"


def test_create_student_duplicate_id():
    duplicate_student = {
        "student_id": "S100001",
        "name": "Duplicate Student",
        "email": "duplicate@deakin.edu.au",
        "program": "Master of Information Technology"
    }

    response = client.post("/students", json=duplicate_student)

    assert response.status_code == 400
    assert response.json()["detail"] == "Student ID already exists"