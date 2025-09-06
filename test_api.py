# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 00:52:44 2025

@author: chand
"""

import requests

# Base URL
BASE = "http://127.0.0.1:5000"

# Test: Register Student
response = requests.post(BASE + "/register_student", json={
    "name": "Alice",
    "college_id": 1
})
print("Register Student:", response.json())

# Test: Create Event
response = requests.post(BASE + "/create_event", json={
    "title": "Hackathon",
    "type": "Tech",
    "college_id": 1
})
print("Create Event:", response.json())
# Test: Mark Attendance
response = requests.post(BASE + "/mark_attendance", json={
    "student_id": 1,
    "event_id": 1,
    "status": "present"
})
print("Mark Attendance:", response.json())

# Test: Submit Feedback
response = requests.post(BASE + "/submit_feedback", json={
    "student_id": 1,
    "event_id": 1,
    "rating": 5
})
print("Submit Feedback:", response.json())

# Test: Get Reports
print("Registrations Report:", requests.get(BASE + "/report/registrations").json())
print("Attendance Report:", requests.get(BASE + "/report/attendance").json())
print("Feedback Report:", requests.get(BASE + "/report/feedback").json())
# Register Alice to Hackathon
response = requests.post(BASE + "/mark_attendance", json={
    "student_id": 1,
    "event_id": 1,
    "status": "present"
})
print("Mark Attendance:", response.json())
