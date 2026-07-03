# Week 01 - Basic FastAPI Application Example

This repository contains a minimal FastAPI application designed to help you set up and verify your Python development environment for the unit. It serves as a simple "hello world" to ensure `Python`, `pip`, `venv`, `FastAPI`, and `Uvicorn` are installed and working correctly.

## Prerequisites

Before you begin, ensure you have the following installed:

- `Python`

- `pip` (Python package installer, usually comes with Python)

- `venv` (Python module for creating virtual environments, usually comes with Python)

## Setup and Run Instructions

Follow these steps to get the basic FastAPI application running on your local machine:

1. Clone the Repository:
   If you haven't already, clone the unit's example code repository to your local machine:

```bash
git clone https://github.com/sit722-devops/week01.git
```

2. Then navigate into the `week01` directory:

```bash
cd week01
```

3. Create and Activate a Python Virtual Environment:

It's best practice to use a virtual environment to manage project dependencies.

```bash
# Create the virtual environment
python -m venv .venv

# Activate the virtual environment
# On macOS/Linux:
source ./.venv/bin/activate
# On Windows (Command Prompt):
# .\.venv\Scripts\activate.bat
# On Windows (PowerShell):
# .\.venv\Scripts\Activate.ps1
```

You should see `(.venv)` prefixing your terminal prompt, indicating the virtual environment is active.

4. Install Dependencies:

With your virtual environment activated, install the required Python packages:

```bash
pip install -r requirements.txt
```

5. Update Your Information in `students.py`

Open the `students.py` file in your VS Code editor. Update the placeholder information (<STUDENT_ID>, <STUDENT_NAME>, <STUDENT_EMAIL> and <STUDENT_PROGRAM>) with your actual details. Save the file after making these changes.

6. Run unit tests

Before running the application, execute the unit tests to verify that your changes have not introduced any issues.

```bash
pytest tests
```

Ensure that all tests pass successfully before proceeding to the next step.

7. Run the FastAPI Application:

Start the FastAPI application using Uvicorn:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
#### Command explanation

- `main:app`: Specifies that Uvicorn should look for an app object (your FastAPI instance) within the app.py file.

- `--reload`: Enables auto-reloading of the server on code changes (useful for development).

- `--host 0.0.0.0`: Makes the application accessible from outside localhost (e.g., from other devices on your local network, or from Docker containers if you later integrate).

- `--port 8000`: Specifies the port the application will listen on.

8. Access the Application in Your Browser:

Open your web browser and navigate to the following URLs:

- Root Endpoint: `http://localhost:8000/`
- Swagger API Documentation: `http://localhost:8000/docs`

Verify that:

- The application starts successfully.
- Your updated student information is displayed correctly.
- The API documentation loads without any errors.


## Expected Outcome
By completing this exercise, you should be able to:

- Set up a Python development environment.
- Create and activate a Python virtual environment.
- Install project dependencies.
- Update application data.
- Execute unit tests.
- Run a FastAPI application locally.
- Access and test REST APIs using the FastAPI Swagger interface.


**Congratulations! Your basic FastAPI development environment is set up and working.**
