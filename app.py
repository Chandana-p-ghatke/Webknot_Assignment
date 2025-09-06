# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 00:17:05 2025

@author: chand
"""

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# ---------- Database Initialization ----------
def init_db():
    conn = sqlite3.connect("campus.db")
    cur = conn.cursor()

    # Students
    cur.execute("""CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    college_id INT)""")

    # Events
    cur.execute("""CREATE TABLE IF NOT EXISTS events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    type TEXT,
                    college_id INT)""")

    # Registrations
    cur.execute("""CREATE TABLE IF NOT EXISTS registrations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id INT,
                    event_id INT)""")

    # Attendance
    cur.execute("""CREATE TABLE IF NOT EXISTS attendance (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id INT,
                    event_id INT,
                    status TEXT)""")

    # Feedback
    cur.execute("""CREATE TABLE IF NOT EXISTS feedback (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id INT,
                    event_id INT,
                    rating INT)""")

    conn.commit()
    conn.close()

# ---------- Routes ----------
@app.route("/")
def home():
    return "Campus Event System Running 🎓"

# Register Student
@app.route("/register_student", methods=["POST"])
def register_student():
    data = request.json
    conn = sqlite3.connect("campus.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO students (name, college_id) VALUES (?, ?)",
                (data["name"], data["college_id"]))
    conn.commit()
    conn.close()
    return jsonify({"message": f"Student {data['name']} registered successfully!"})

# Create Event
@app.route("/create_event", methods=["POST"])
def create_event():
    data = request.json
    conn = sqlite3.connect("campus.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO events (title, type, college_id) VALUES (?, ?, ?)",
                (data["title"], data["type"], data["college_id"]))
    conn.commit()
    conn.close()
    return jsonify({"message": f"Event '{data['title']}' created successfully!"})

# Mark Attendance
@app.route("/mark_attendance", methods=["POST"])
def mark_attendance():
    data = request.json
    conn = sqlite3.connect("campus.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO attendance (student_id, event_id, status) VALUES (?, ?, ?)",
                (data["student_id"], data["event_id"], data["status"]))
    conn.commit()
    conn.close()
    return jsonify({"message": "Attendance marked successfully!"})

# Submit Feedback
@app.route("/submit_feedback", methods=["POST"])
def submit_feedback():
    data = request.json
    conn = sqlite3.connect("campus.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO feedback (student_id, event_id, rating) VALUES (?, ?, ?)",
                (data["student_id"], data["event_id"], data["rating"]))
    conn.commit()
    conn.close()
    return jsonify({"message": "Feedback submitted successfully!"})

# ---------- Reports ----------
@app.route("/report/registrations", methods=["GET"])
def report_registrations():
    conn = sqlite3.connect("campus.db")
    cur = conn.cursor()
    cur.execute("SELECT e.title, COUNT(r.id) FROM events e LEFT JOIN registrations r ON e.id = r.event_id GROUP BY e.id")
    result = cur.fetchall()
    conn.close()
    return jsonify(result)

@app.route("/report/attendance", methods=["GET"])
def report_attendance():
    conn = sqlite3.connect("campus.db")
    cur = conn.cursor()
    cur.execute("SELECT e.title, a.status, COUNT(a.id) FROM events e LEFT JOIN attendance a ON e.id = a.event_id GROUP BY e.id, a.status")
    result = cur.fetchall()
    conn.close()
    return jsonify(result)

@app.route("/report/feedback", methods=["GET"])
def report_feedback():
    conn = sqlite3.connect("campus.db")
    cur = conn.cursor()
    cur.execute("SELECT e.title, AVG(f.rating) FROM events e LEFT JOIN feedback f ON e.id = f.event_id GROUP BY e.id")
    result = cur.fetchall()
    conn.close()
    return jsonify(result)

# ---------- Main ----------
if __name__ == "__main__":
    init_db()
    app.run(debug=True)

