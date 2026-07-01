# week01/main.py - Basic FastAPI Application for Environment Setup Task

from fastapi import FastAPI  # Import the FastAPI

# Create an instance of the FastAPI application
# This is the main entry point for your web service.
app = FastAPI(
    title="Week 01 Basic API",
    description="A very simple FastAPI application to test environment setup.",
    version="1.0.0",
)


# Define a root endpoint (GET request to '/')
# When a client accesses the root URL, this function will be called.
@app.get("/")
async def read_root():
    """
    Returns a welcome message for the API.
    """
    return {"message": "Welcome to the basic Week 01 FastAPI application!"}


# Define another GET endpoint to return some student information
# This endpoint will be accessed at '/student_info'
@app.get("/student_info")
async def get_student_info():
    """
    Returns a dictionary with mock student information.
    This demonstrates returning simple JSON data.
    """
    return {
        "student_name": "<YOUR_NAME>",
        "student_id": "<YOUR_STUDENT_ID>",
        "unit_code": "SIT722",
        "unit_name": "Software Deployment and Operation",
        "campus": "<YOUR_CAMPUS>",
        "year": 2026,
    }
