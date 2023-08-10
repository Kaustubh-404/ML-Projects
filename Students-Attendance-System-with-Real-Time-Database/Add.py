import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':""
})

ref = db.reference('Students')


data = {
    "S5501":
    {
        "Name": "Elon Musk",
        "Major": "Physics",
        "Starting_Year": 2017,
        "Total-Attendance":10,
        "Last_attendance_time":"2023-03-17 15:30:00",
        "Academic-Year": 4
    },
    "S5506":
    {
        "Name": "Kaustubh Pardeshi",
        "Major": "Computer",
        "Starting_Year": 2021,
        "Total-Attendance":10,
        "Last_attendance_time":"2023-03-17 15:30:00",
        "Academic-Year": 2
    },
    "S5517":
    {
        "Name": "Rutuja Patil",
        "Major": "Computer ",
        "Starting_Year": 2021,
        "Total-Attendance":10,
        "Last_attendance_time":"2023-03-17 15:30:00",
        "Academic-Year": 2
    },
    "S5507":
    {
        "Name": "Meet Mavani",
        "Major": "Computer",
        "Starting_Year": 2021,
        "Total-Attendance":10,
        "Last_attendance_time":"2023-03-17 15:30:00",
        "Academic-Year": 2
    },
    "S5508":
    {
        "Name": "Parth Shelar",
        "Major": "Electronics",
        "Starting_Year": 2021,
        "Total-Attendance":10,
        "Last_attendance_time":"2023-03-17 15:30:00",
        "Academic-Year": 2
    },
    "S5552":
    {
        "Name": "Shruti Sharma",
        "Major": "Computer",
        "Starting_Year": 2021,
        "Total-Attendance":10,
        "Last_attendance_time":"2023-03-17 15:30:00",
        "Academic-Year": 2
    }

}

for key,value in data.items():
    ref.child(key).set(value)
