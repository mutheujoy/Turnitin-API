# app.py

from flask import Flask, jsonify, request
from flask_cors import CORS
import turnitin

app = Flask(__name__)
CORS(app)

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    try:
        auth = turnitin.login(data["email"], data["password"])
        return jsonify({"auth": auth})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/courses", methods=["GET"])
def get_courses():
    auth_token = request.headers.get('Authorization')
    try:
        courses = turnitin.get_courses(auth_token)
        return jsonify({"courses": courses})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/assignments/<course_id>", methods=["GET"])
def get_assignments(course_id):
    auth_token = request.headers.get('Authorization')
    try:
        assignments = turnitin.get_assignments(auth_token, course_id)
        return jsonify({"assignments": assignments})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/download/<assignment_id>", methods=["GET"])
def download_assignment(assignment_id):
    auth_token = request.headers.get('Authorization')
    try:
        submission = turnitin.download_submission(auth_token, assignment_id)
        return jsonify({"submission": submission})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/submit", methods=["POST"])
def submit_document():
    data = request.get_json()
    auth_token = request.headers.get('Authorization')
    try:
        submission_id = turnitin.submit_document(auth_token, data)
        return jsonify({"submission_id": submission_id})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
