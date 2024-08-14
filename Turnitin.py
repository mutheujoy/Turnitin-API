# turnitin.py

import requests
from bs4 import BeautifulSoup
import time
import re

BASE_URL = "https://api.turnitin.com"

def login(email, password):
    # Simulate a login process to obtain an auth token
    session = requests.Session()
    login_url = f"{BASE_URL}/api/login"
    response = session.post(login_url, json={"email": email, "password": password})
    response.raise_for_status()
    return response.json()["auth_token"]

def get_courses(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.get(f"{BASE_URL}/api/courses", headers=headers)
    response.raise_for_status()
    return response.json()["courses"]

def get_assignments(auth_token, course_id):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.get(f"{BASE_URL}/api/courses/{course_id}/assignments", headers=headers)
    response.raise_for_status()
    return response.json()["assignments"]

def download_submission(auth_token, assignment_id):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.get(f"{BASE_URL}/api/assignments/{assignment_id}/submissions", headers=headers)
    response.raise_for_status()
    return response.json()["submissions"]

def submit_document(auth_token, data):
    headers = {"Authorization": f"Bearer {auth_token}", "Content-Type": "application/json"}
    response = requests.post(f"{BASE_URL}/api/submit", headers=headers, json=data)
    response.raise_for_status()
    return response.json()["submission_id"]
