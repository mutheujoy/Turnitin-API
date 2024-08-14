# Turnitin API

A REST API for Turnitin.com.

## Built by Ronak Badhe / Kento Nishi

### Endpoints

- **/login**: Authenticate with Turnitin.
- **/courses**: Retrieve available courses.
- **/assignments**: Get assignments for a course.
- **/download**: Download assignment submissions.
- **/submit**: Submit a document to Turnitin.

## Getting Started

### Prerequisites

- Python 3.x
- Virtualenv

### Installation

```bash
pip install -r requirements.txt

### Running the API
```bash
python app.py

### Usage
```bash
import requests

url = "http://localhost:5000"

USERNAME = "email@example.com"
PASSWORD = "password"

with requests.Session() as s:
    login_result = s.post(url + "/login", json={
        "email": USERNAME,
        "password": PASSWORD
    })
    auth = login_result.json()

    # Get courses
    courses_result = s.get(url + "/courses", headers={"Authorization": auth["auth"]})
    courses = courses_result.json()

    # Get assignments for the first course
    course_id = courses["courses"][0]["id"]
    assignments_result = s.get(url + f"/assignments/{course_id}", headers={"Authorization": auth["auth"]})
    assignments = assignments_result.json()

    # Download a submission
    assignment_id = assignments["assignments"][0]["id"]
    submission_result = s.get(url + f"/download/{assignment_id}", headers={"Authorization": auth["auth"]})
    submission = submission_result.json()

    # Submit a document
    submission_data = {
        "course_id": course_id,
        "title": "Sample Submission",
        "file": "document_content"
    }
    submit_result = s.post(url + "/submit", headers={"Authorization": auth["auth"]}, json=submission_data)
    submission_id = submit_result.json()

